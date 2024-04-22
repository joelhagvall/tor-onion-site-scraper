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

if __name__ == "__main__":  #Kört till 15e hittils 
    urls = [
        "https://euqrjceb3fa3o2rxjuqqkx76qjreqjlvtidfpgfyv6cd4z22hybnccyd.onion/",
        "http://2dhhwu7c5u4wdzn3bzqxfmygyqdushy56dnknkfexhze4sot5ljkd.onion/",
        "http://2dhhwu7c5u4wdzn3bzqxfmygyqdushy56dnknkfexhze4sot5ljkd3yd.onion/",
        "http://wzxwaen2zhuouiirspgpaw7hjvIzini5bfmopb6e45mkj5exbzzossad.onion/viewtopic.php?t=10&sid=7ab461c47bbc12467e55093036839f70.onion",
        "http://wzxwaen2zhuouirspgpaw7hjvlzini5bfmopb6e45mkj5exbzzossad.onion/viewtopic.php?t=204",
        "http://alphvmmm2703abo3r2mImjrpdmzle3rykajqc5xsj7j7ejksbpsa36ad.onion/",
        "http://spywrfsmz6h66kcl56jl73s6uqimxu6oo3hym7zrf5myznol4qwwgoid.onion/",
        "http://pinr7nwvdaehemcrpgcjqf4fooit3c4gjw6dhzrp443ctvnoad.onion",
        "http://hackingbr3v6yj5pci6im57ud52vqfygg4swvbj7vmqgfncqpwaul3qd.onion/",
        "http://cus43oder3dcj5whshor5kbprvj6fjciupurb5v5vamzjapiruy3coid.onion/"
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



