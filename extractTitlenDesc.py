import requests
import csv
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def fetch_onion_site_html(url, session):
    try:
        response = session.get(url)
        response.raise_for_status()  # Raises an exception for HTTP errors
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

def scrape_category_page(category_url, session):
    html_content = fetch_onion_site_html(category_url, session)
    if html_content is None:
        return []

    soup = BeautifulSoup(html_content, 'html.parser')
    all_items = []

    # Extract title and description from each item on the page
    for item in soup.find_all('div', class_='item'):
        title = item.find('div', class_='title').text.strip() if item.find('div', class_='title') else 'No Title'
        description = item.find('div', class_='description').text.strip() if item.find('div', class_='description') else 'No Description'
        all_items.append([title, description])

    return all_items

if __name__ == "__main__":
    category_url = "http://ddockkkwl45kmnnd7b332qu4h3ov66e3zy2ytrpfarpswvtldcx3cvad.onion/category/civil_softwares"
    session = requests.session()
    session.proxies = {'http': 'socks5h://localhost:9050', 'https': 'socks5h://localhost:9050'}

    items = scrape_category_page(category_url, session)
    
    # Save extracted data to CSV
    with open('results.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'Description'])
        writer.writerows(items)
    
    print(f"Total items scraped: {len(items)}")
