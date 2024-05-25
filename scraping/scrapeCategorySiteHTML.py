import requests
import os
import time
import random
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.3",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.3"
]


""" function retrieve_site() fetches the URL and retries if failed, using randomized user agents to appear less like a bot."""
def retrieve_site(url, session, retries=3, backoff_factor=0.5):
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
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"Error fetching {url}: {e}")
            time.sleep(5)
    return None



""" The function save_html() writes the content to the specified path."""
def save_html(content, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"Saved HTML content to {path}")



""" Function is_valid_link() checks if the URL is correct."""
def is_valid_link(url, domain, category_path):
    return urlparse(url).netloc == domain and category_path in urlparse(url).path



""" The function scrape_category_site() scrapes everything visible, including going through each product and its href tag.
    Timers are used in order to prevent being banned from the site due to bot activity.
    The output is created directories for the category with HTML-files for each category indexed page, and HTML-files for every
    product page as well. """
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

            html_content = retrieve_site(current_url, session)
            if html_content is not None:
                pass
            else:
                site_successful = False
                continue

            page_filename = os.path.join(base_path,
                                         f"{len(visited)}_{urlparse(current_url).path.strip('/').replace('/', '_') or 'index.html'}")
            save_html(html_content, page_filename)

            soup = BeautifulSoup(html_content, 'html.parser')

            for link in soup.find_all('a', href=True):
                full_link = urljoin(current_url, link['href'])
                if 'product' in full_link:
                    if full_link not in visited:
                        product_html = retrieve_site(full_link, session)
                        if product_html:
                            product_filename = os.path.join(base_path,
                                                            f"{len(visited)}_{urlparse(full_link).path.strip('/').replace('/', '_')}.html")
                            save_html(product_html, product_filename)
                        visited.add(full_link)
                    elif is_valid_link(full_link, domain, category_path) and full_link not in visited:
                        to_visit.append(full_link)
                elif is_valid_link(full_link, domain, category_path) and full_link not in visited:
                    to_visit.append(full_link)

            time.sleep(random.uniform(1, 5))

    return site_successful, "Failed to fetch some pages" if not site_successful else "Success"


if __name__ == "__main__":
    base_url = "http://oirolrkrppy6sei6x6bvkkdolc4cjqzqfhxisfzu6exqblahwrrvktyd.onion"
    category = "accounts"

    session = requests.session()
    session.proxies = {'http': 'socks5h://localhost:9050', 'https': 'socks5h://localhost:9050'}

    base_directory = f"new_onion_sites_html/{category}"
    if not os.path.exists(base_directory):
        os.makedirs(base_directory)
    else:
        pass

    success, message = scrape_category_site(base_url, category, session, base_directory)
    status = "❌" if not success else "✅"
    print(f"Final status of category '{category}': {status}")
