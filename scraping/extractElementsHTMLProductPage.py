import os
import csv
from bs4 import BeautifulSoup

def extract_from_html_files(directory):
    unique_items = []  # Use a list to store unique items
    
    # Iterate through all files in the directory
    for filename in os.listdir(directory):
        if "1_category_drugs_production" in filename or "category" in filename or "product" not in filename:
            continue  # Skip unwanted files

        filepath = os.path.join(directory, filename)
        if not os.path.isfile(filepath):  # Check if it's a file
            continue
        
        with open(filepath, "r", encoding="utf-8") as file:
            html_content = file.read()
            soup = BeautifulSoup(html_content, 'html.parser')

            # Extract the first and second occurrence of div class 'heading'
            headings = soup.find_all('div', class_='heading', limit=2)
            heading_text = headings[0].text.strip().replace('\n', ' ').replace(',', ' ') if len(headings) > 0 else ''
            comment_text = headings[1].text.strip().replace('\n', ' ').replace(',', ' ') if len(headings) > 1 else ''

            # Extract contents from different divs, leave blank if not found
            tab1_text = soup.find('div', class_='tab1').text.strip().replace('\n', ' ').replace(',', ' ') if soup.find('div', class_='tab1') else ''
            tab2_text = soup.find('div', class_='tab2').text.strip().replace('\n', ' ').replace(',', ' ') if soup.find('div', class_='tab2') else ''
            price_text = soup.find('div', class_='price').text.strip().replace('\n', ' ').replace(',', ' ') if soup.find('div', class_='price') else ''
            stats_text = soup.find('div', class_='stats').text.strip().replace('\n', ' ').replace(',', ' ') if soup.find('div', class_='stats') else ''
            comment_info_text = soup.find('div', class_='comments').text.strip().replace('\n', ' ').replace(',', ' ') if soup.find('div', class_='comments') else ''

            unique_items.append([heading_text, tab1_text, tab2_text, price_text, stats_text, comment_text, comment_info_text])

    return unique_items

if __name__ == "__main__":
    categories = [
        "civil_softwares",
        "tutorials",
        "confidential_info",
        "cards_and_cvv",
        "hacks",
        "application_software",
        "accounts",
        "documents",
        "false_documents",
        "exploit_kit",
        "drop_bank",
        "security",
        "system_software",
        "utilities",
        "software_forensics_tools",
        "forgery",
        "network_services",
        "database",
        "leaked_documents",
        "digital_forensics",
        "0day",
        "intelligence",
        "private_security",
        "racketeering"
    ]

    results_directory = "./productPageResultsHTML/"
    os.makedirs(results_directory, exist_ok=True)  # Create the directory if it doesn't exist

    for category in categories:
        directory = f"./new_onion_sites_html/{category}/"  # Use f-string to make the category name dynamic
        items = extract_from_html_files(directory)

        csv_filepath = os.path.join(results_directory, f"{category}.csv")  # Use f-string to make the CSV filename dynamic
        if os.path.exists(csv_filepath):
            print(f"\U0001F4C1 CSV file for {category} already exists.")
        else:
            try:
                with open(csv_filepath, 'w', newline='', encoding='utf-8') as file:
                    writer = csv.writer(file)
                    writer.writerow(['Heading', 'Tab1', 'Tab2', 'Price', 'Stats', 'Comment', 'CommentInfo'])
                    writer.writerows(items)
                print(f"\U00002705 CSV file for {category} created successfully.")
            except Exception as e:
                print(f"\U0000274C Error creating CSV file for {category}: {e}")

    print("CSV creation process completed.")
