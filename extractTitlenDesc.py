import requests
import os
import csv
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

def scrape_category_site(base_url, category, session, base_path):
    category_url = f"{base_url}/category/{category}"
    domain = urlparse(category_url).netloc
    visited = set()
    to_visit = [category_url]
    all_items = []
    max_items = 10  # Maximum number of items to scrape

    while to_visit and len(all_items) < max_items:
        current_url = to_visit.pop(0)
        if current_url in visited:
            continue
        visited.add(current_url)

        html_content = fetch_onion_site_html(current_url, session)
        if html_content is None:
            continue

        soup = BeautifulSoup(html_content, 'html.parser')

        # Extract title and description from each item on the page
        for item in soup.find_all('div', class_='item'):
            title = item.find('div', class_='title').text.strip() if item.find('div', class_='title') else 'No Title'
            description = item.find('div', class_='description').text.strip() if item.find('div', class_='description') else 'No Description'
            all_items.append([title, description])
            if len(all_items) >= max_items:
                break

        # Find and process all navigable links
        for link in soup.find_all('a', href=True):
            full_link = urljoin(current_url, link['href'])
            if is_valid_link(full_link, domain, f"/category/{category}") and full_link not in visited:
                to_visit.append(full_link)

    # Save extracted data to CSV
    with open(os.path.join(base_path, 'results.csv'), 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'Description'])
        writer.writerows(all_items[:max_items])

    return len(all_items), "Success"

def is_valid_link(url, domain, category_path):
    return urlparse(url).netloc == domain and category_path in urlparse(url).path

if __name__ == "__main__":
    base_url = "http://ddockkkwl45kmnnd7b332qu4h3ov66e3zy2ytrpfarpswvtldcx3cvad.onion/"
    category = "civil_softwares"
    session = requests.session()
    session.proxies = {'http': 'socks5h://localhost:9050', 'https': 'socks5h://localhost:9050'}
    base_directory = f"onion_sites_html/{urlparse(base_url).netloc}/{category}"
    os.makedirs(base_directory, exist_ok=True)

    total_items, message = scrape_category_site(base_url, category, session, base_directory)
    print(f"Total items scraped: {total_items}")
    print(f"Final status of category '{category}': {message}")
