import requests
import os
import time
import random
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# List of user agents to rotate
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.3",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.3"
]

def fetch_onion_site_html(url, session, retries=3, backoff_factor=0.5):
    retry_strategy = Retry(
        total=retries,
        backoff_factor=backoff_factor,
        status_forcelist=[500, 502, 503, 504],
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount('http://', adapter)
    session.mount('https://', adapter)

    for _ in range(retries):
        try:
            response = session.get(url, headers={'User-Agent': random.choice(USER_AGENTS)})
            response.raise_for_status()  # Raise an exception for HTTP errors
            return response.text
        except requests.RequestException as e:
            print(f"Error fetching {url}: {e}")
            time.sleep(5)  # Pause for 5 seconds before retrying
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
        if current_url not in visited:
            visited.add(current_url)

            html_content = fetch_onion_site_html(current_url, session)
            if html_content is not None:
                pass
            else:
                site_successful = False
                continue

            # Save the current page
            page_filename = os.path.join(base_path, f"{len(visited)}_{urlparse(current_url).path.strip('/').replace('/', '_') or 'index.html'}")
            save_html(html_content, page_filename)

            soup = BeautifulSoup(html_content, 'html.parser')

            # Parse the page to find links and handle "View" divs for product pages
            for link in soup.find_all('a', href=True):
                full_link = urljoin(current_url, link['href'])
                if 'product' in full_link and full_link not in visited:
                    product_html = fetch_onion_site_html(full_link, session)
                    if product_html:
                        product_filename = os.path.join(base_path, f"{len(visited)}_{urlparse(full_link).path.strip('/').replace('/', '_')}.html")
                        save_html(product_html, product_filename)
                    visited.add(full_link)
                elif is_valid_link(full_link, domain, category_path) and full_link not in visited:
                    to_visit.append(full_link)

            # Pause for a random duration between 1 to 5 seconds
            time.sleep(random.uniform(1, 5))

    return site_successful, "Success" if site_successful else "Failed to fetch some pages"

if __name__ == "__main__":  
    base_url = "http://oirolrkrppy6sei6x6bvkkdolc4cjqzqfhxisfzu6exqblahwrrvktyd.onion"
    category = "about"

    session = requests.session()
    session.proxies = {'http': 'socks5h://localhost:9050', 'https': 'socks5h://localhost:9050'}

    base_directory = f"new_onion_sites_html/{category}"
    if os.path.exists(base_directory):
        pass
    else:
        os.makedirs(base_directory)

    success, message = scrape_category_site(base_url, category, session, base_directory)
    status = "✅" if success else "❌"
    print(f"Final status of category '{category}': {status}")
