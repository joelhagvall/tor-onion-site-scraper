import os
import random
import time
from urllib.parse import urlparse

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# List of user agents to rotate
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.3",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.3"
]

""" The function retrieve_site() connects to the specified URL with randomized user agents
to prevent bot-like activity. 
"""


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


""" Function save_html() saves the HTML of the specified URL. 
"""


def save_html(content, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"Saved HTML content to {path}")


""" Function scrape_single_page() fetches the site from retrieve_site() function and saves the site using save_html() 
function. """


def scrape_single_page(url, session, base_path):
    html_content = retrieve_site(url, session)
    if html_content is not None:
        # Save the fetched page
        page_filename = os.path.join(base_path, f"{urlparse(url).path.strip('/').replace('/', '_') or 'index.html'}")
        save_html(html_content, page_filename)
        return True, "Success"
    else:
        return False, "Failed to fetch the page"


if __name__ == "__main__":
    base_url = "http://oirolrkrppy6sei6x6bvkkdolc4cjqzqfhxisfzu6exqblahwrrvktyd.onion/faq"
    nested_directory = "faq"

    session = requests.session()
    session.proxies = {'http': 'socks5h://localhost:9050', 'https': 'socks5h://localhost:9050'}

    base_directory = os.path.join("new_onion_sites_html", nested_directory)
    if os.path.exists(base_directory):
        pass
    else:
        os.makedirs(base_directory)

    success, message = scrape_single_page(base_url, session, base_directory)
    status = "❌" if not success else "✅"
    print(f"Final status: {status}")
