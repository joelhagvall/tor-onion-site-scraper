import os
import csv
from bs4 import BeautifulSoup

def extract_from_html_files(directory):
    unique_items = []  # Use a list to store unique items
    
    # Iterate through all files in the directory
    for filename in os.listdir(directory):
        if "1_category_drugs_production" not in filename:
            if "category" in filename:
                continue  # Skip files that contain "category" in their names
            if "product" not in filename:
                continue  # Skip files that don't contain "product" in their names

            filepath = os.path.join(directory, filename)
            if not os.path.isfile(filepath):  # Check if it's a file
                continue
            with open(filepath, "r", encoding="utf-8") as file:
                html_content = file.read()
                soup = BeautifulSoup(html_content, 'html.parser')

                # Extract the first and second occurrence of div class 'heading'
                headings = soup.find_all('div', class_='heading', limit=2)
                heading_text = headings[0].text.strip() if len(headings) > 0 else ''
                comment_text = headings[1].text.strip() if len(headings) > 1 else ''

                tab1_content = soup.find('div', class_='tab1')
                tab2_content = soup.find('div', class_='tab2')
                price_content = soup.find('div', class_ = 'price')
                stats_content = soup.find('div', class_ = 'stats')
                
                # Extract the comment information
                comment_info = soup.find('div', class_='comments')
                comment_info_text = comment_info.text.strip() if comment_info else ''

                if tab1_content and tab2_content and price_content and stats_content:
                    tab1_text = tab1_content.text.strip()
                    tab2_text = tab2_content.text.strip()
                    price_text = price_content.text.strip()
                    stats_text = stats_content.text.strip()
                    unique_items.append([heading_text, tab1_text, tab2_text, price_text, stats_text, comment_text, comment_info_text])

    return unique_items

if __name__ == "__main__":
    category = "civil_softwares"  # Define the category name
    directory = f"./new_onion_sites_html/{category}/"  # Use f-string to make the category name dynamic
    items = extract_from_html_files(directory)

    # Save extracted data to CSV in the "results" directory
    results_directory = "./productPageResultsHTML/"
    os.makedirs(results_directory, exist_ok=True)  # Create the directory if it doesn't exist
    csv_filepath = os.path.join(results_directory, f"{category}.csv")  # Use f-string to make the CSV filename dynamic
    with open(csv_filepath, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Heading', 'Tab1', 'Tab2', 'Price', 'Stats', 'Comment', 'CommentInfo'])
        writer.writerows(items)
    
    print(f"Total unique items extracted from HTML files: {len(items)}")
