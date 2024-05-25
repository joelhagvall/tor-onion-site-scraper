import os
import csv
from bs4 import BeautifulSoup

""" Function extract_html_prod() goes through HTML-files in directory "new_onion_sites_html" and its specified category's
directory, and iterates through to find files with "product" in them. This represents every product listing belonging
to a specified category on the page.

The elements of relevancy for our thesis are Heading, Tab1, Tab2, and Comments. Heading and Tab1 are the site's classes
and represents each product's title and description respectively. Tab2 represents the refund policy. 

One comment regarding Heading - the Heading element appears twice in the file, the first occurrence is related 
to the title and description altogether, the second occurrence is related to the Comments(0) element. 
The program ignores if more occurrences of Heading is found, since it is related to the "Related Products" section of
the site. 

The elements are extracted and pasted in to a new CSV-file. Given the observation, all product's are built this way,
and if one or two elements would be missing, then the CSV-file writes the field as blank.
"""


def extract_html_prod(curr_dir):
    unique_items = []

    # Iterate through all files in the directory
    for filename in os.listdir(curr_dir):
        if "1_category_drugs_production" in filename:   # This file is generated automatically for the categories and can be ignored.
            continue
        if "category" in filename:
            continue
        if "product" in filename:
            filepath = os.path.join(curr_dir, filename)
            if not os.path.isfile(filepath):
                continue

            with open(filepath, "r", encoding="utf-8") as file:
                html_content = file.read()
                soup = BeautifulSoup(html_content, 'html.parser')

                headings = soup.find_all('div', class_='heading', limit=2)
                heading_text = headings[0].text.strip().replace('\n', ' ').replace(',', ' ') if len(
                    headings) > 0 else ''
                comment_text = headings[1].text.strip().replace('\n', ' ').replace(',', ' ') if len(
                    headings) > 1 else ''

                tab1_text = soup.find('div', class_='tab1').text.strip().replace('\n', ' ').replace(',',
                                                                                                    ' ') if soup.find(
                    'div', class_='tab1') else ''
                tab2_text = soup.find('div', class_='tab2').text.strip().replace('\n', ' ').replace(',',
                                                                                                    ' ') if soup.find(
                    'div', class_='tab2') else ''
                comment_info_text = soup.find('div', class_='comments').text.strip().replace('\n', ' ').replace(',',
                                                                                                                ' ') if soup.find(
                    'div', class_='comments') else ''

                unique_items.append(
                    [heading_text, tab1_text, tab2_text, comment_text, comment_info_text])

    return unique_items


if __name__ == "__main__":
    categories = [  # Our 24 chosen categories.
        "civil_softwares", "tutorials", "confidential_info", "cards_and_cvv",
        "hacks", "application_software", "accounts", "documents",
        "false_documents", "exploit_kit", "drop_bank", "security",
        "system_software", "utilities", "software_forensics_tools", "forgery",
        "network_services", "database", "leaked_documents", "digital_forensics",
        "0day", "intelligence", "private_security", "racketeering"
    ]

    results_directory = "./productPageResultsHTML/"
    os.makedirs(results_directory, exist_ok=True)

    for category in categories:
        directory = f"./new_onion_sites_html/{category}/"
        items = extract_html_prod(directory)

        csv_filepath = os.path.join(results_directory,
                                    f"{category}.csv")
        if not os.path.exists(csv_filepath):
            try:
                with open(csv_filepath, 'w', newline='', encoding='utf-8') as file:
                    writer = csv.writer(file)
                    writer.writerow(['Heading', 'Tab1', 'Tab2', 'Comment', 'CommentInfo'])
                    writer.writerows(items)
                print(f"CSV file for {category} created successfully.")
            except Exception as e:
                print(f"Error creating CSV file for {category}: {e}")
        else:
            print(f"CSV file for {category} has already been created.")

    print("All CSV-files have been created successfully.")
