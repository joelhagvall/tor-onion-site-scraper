import requests
import csv
import time
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def fetch_onion_site_html(url, session, max_retries=5, delay=3):
    for attempt in range(max_retries):
        try:
            response = session.get(url)
            response.raise_for_status()  # Raises an exception for HTTP errors
            return response.text
        except requests.RequestException as e:
            print(f"Attempt {attempt + 1}: Error fetching {url}: {e}")
            time.sleep(delay)  # Wait before trying again
    print(f"Failed to fetch {url} after {max_retries} attempts.")
    return None

def scrape_limited_pages(base_url, session, max_pages):
    page_number = 1
    unique_items = {}  # Use a dictionary to store unique items
    while page_number <= max_pages:
        url = f"{base_url}/{page_number}" if page_number > 1 else base_url
        html_content = fetch_onion_site_html(url, session)
        if html_content is None:
            print(f"Skipping page {page_number} due to repeated fetch failures.")
            page_number += 1
            continue

        soup = BeautifulSoup(html_content, 'html.parser')

        # Extract title and description from each item on the page
        for item in soup.find_all('div', class_='item'):
            title = item.find('div', class_='title').text.strip() if item.find('div', class_='title') else 'No Title'
            description = item.find('div', class_='description').text.strip() if item.find('div', class_='description') else 'No Description'
            unique_key = f"{title}|{description}"  # Create a unique key for each item

            if unique_key not in unique_items:
                unique_items[unique_key] = [title, description]

        page_number += 1

    return list(unique_items.values())  # Convert the dictionary values to a list

if __name__ == "__main__":
    base_url = "http://ddockkkwl45kmnnd7b332qu4h3ov66e3zy2ytrpfarpswvtldcx3cvad.onion/category/leaked_documents/"
    session = requests.session()
    session.proxies = {'http': 'socks5h://localhost:9050', 'https': 'socks5h://localhost:9050'}
    
    max_pages = 2  # Maximum number of pages to scrape
    items = scrape_limited_pages(base_url, session, max_pages)
    
    # Save extracted data to CSV
    with open('resultsFullLeaked_Documents.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'Description'])
        writer.writerows(items)
    
    print(f"Total unique items scraped from first {max_pages} pages: {len(items)}")
