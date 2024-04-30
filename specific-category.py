import requests
import os
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def fetch_onion_site_html(url, session):
    try:
        response = session.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

def save_html(content, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"Saved HTML content to {path}")

def is_valid_link(url, domain, category_path):
    return urlparse(url).netloc == domain and category_path in urlparse(url).path

def scrape_category_site(base_url, category, session, base_path):
    category_url = f"{base_url}/category/{category}"
    domain = urlparse(category_url).netloc
    category_path = f"/category/{category}"
    visited = set()
    to_visit = [category_url]
    site_successful = True

    while to_visit:
        current_url = to_visit.pop(0)
        if current_url in visited:
            continue
        visited.add(current_url)

        html_content = fetch_onion_site_html(current_url, session)
        if html_content is None:
            site_successful = False
            continue

        # Save the current page
        page_filename = os.path.join(base_path, urlparse(current_url).path.strip('/').replace('/', '_') or 'index.html')
        save_html(html_content, page_filename)

        soup = BeautifulSoup(html_content, 'html.parser')

        # Parse the page to find links and handle "View" divs for product pages
        for link in soup.find_all('a', href=True):
            full_link = urljoin(current_url, link['href'])
            if 'product' in full_link and full_link not in visited:
                product_html = fetch_onion_site_html(full_link, session)
                if product_html:
                    product_filename = os.path.join(base_path, urlparse(full_link).path.strip('/').replace('/', '_') + '.html')
                    save_html(product_html, product_filename)
                visited.add(full_link)
            elif is_valid_link(full_link, domain, category_path) and full_link not in visited:
                to_visit.append(full_link)

    return site_successful, "Success" if site_successful else "Failed to fetch some pages"

if __name__ == "__main__":  
    base_url = "http://ddockkkwl45kmnnd7b332qu4h3ov66e3zy2ytrpfarpswvtldcx3cvad.onion"
    category = "0day"

    session = requests.session()
    session.proxies = {'http': 'socks5h://localhost:9050', 'https': 'socks5h://localhost:9050'}

    base_directory = f"onion_sites_html/{urlparse(base_url).netloc}/{category}"
    if not os.path.exists(base_directory):
        os.makedirs(base_directory)

    success, message = scrape_category_site(base_url, category, session, base_directory)
    status = "✅" if success else "❌"
    print(f"Final status of category '{category}': {status}")
