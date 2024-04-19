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

def is_valid_link(url, domain):
    return urlparse(url).netloc == domain

def scrape_site(url, session, base_path):
    domain = urlparse(url).netloc
    visited = set()
    to_visit = [url]
    site_successful = True

    while to_visit:
        current_url = to_visit.pop(0)
        if current_url in visited:
            continue
        visited.add(current_url)

        html_content = fetch_onion_site_html(current_url, session)
        if html_content is None:
            site_successful = False
            continue  # Skip saving and further processing if fetching failed

        # Save the current page
        page_filename = os.path.join(base_path, urlparse(current_url).path.strip('/').replace('/', '_') or 'index.html')
        save_html(html_content, page_filename)

        # Parse the page to find links
        soup = BeautifulSoup(html_content, 'html.parser')
        for link in soup.find_all('a', href=True):
            full_link = urljoin(current_url, link['href'])
            if is_valid_link(full_link, domain) and full_link not in visited:
                to_visit.append(full_link)
                
    return site_successful, "Success" if site_successful else "Failed to fetch some pages"

if __name__ == "__main__":
    urls = [
        "http://qu4uozvpp3sfnkcdsoesvmzrvzq7wiz463ywmdnjahdmo5ypznim5nid.onion/",
        "http://ranionuqvczpnypve3xle3srlbkn4rxp7eudpe74zddsfjvz3y7vkkyd.onion/",
        "https://duckduckgogg42xjoc72x3sjasowoarfbgcmvfimaftt6twagswzczad.onion/",
        "http://6nhmgdpnyoljh5uzr5kwlatx2u3diou4ldeommfxjz3wkhalzgjqxzqd.onion/",
        "http://6nhmhfgdpnyoljh5uzr5kwlatx2u3diou4ldeommfxjz3wkhalzgjqxzqd.onion/"
    ]

    session = requests.session()
    session.proxies = {'http': 'socks5h://localhost:9050', 'https': 'socks5h://localhost:9050'}

    results = {}
    for url in urls:
        base_directory = f"onion_sites_html/{urlparse(url).netloc}"
        if os.path.exists(base_directory):
            results[url] = "🗂️"  # Folder already exists
            continue
        
        success, message = scrape_site(url, session, base_directory)
        results[url] = "✅" if success else "❌"

    for url, status in results.items():
        print(f"{url} {status}")

    # Print summary of all URLs processed
    print("\nFinal status of all URLs:")
    for url, status in results.items():
        print(f"{url}: {status}")



