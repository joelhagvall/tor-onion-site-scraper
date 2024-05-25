import os
import csv
from bs4 import BeautifulSoup


""" The function extract_category_page() extracts the div classes title and stats from every occurences on the categories
respective indexed page. The output is a CSV file with Title and Stats for every listing."""
def extract_category_page(curr_dir):
    unique_items = {}

    for filename in os.listdir(curr_dir):
        if filename != "1_category_drugs_production.html":  # This file is generated automatically for the categories and can be ignored.
            if "category" in filename:
                pass
            else:
                continue

            filepath = os.path.join(curr_dir, filename)
            if not os.path.isfile(filepath):
                continue
            with open(filepath, "r", encoding="utf-8") as file:
                html_content = file.read()
                soup = BeautifulSoup(html_content, 'html.parser')

                for item in soup.find_all('div', class_='item'):
                    title = 'No Title' if not item.find('div',
                                                        class_='title') else item.find('div', class_='title').text.strip()
                    stats = 'No Stats' if not item.find('div',
                                                        class_='stats') else item.find('div', class_='stats').text.strip()
                    unique_key = f"{title}|{stats}"
                    if unique_key in unique_items:
                        continue
                    unique_items[unique_key] = [title, stats]

    return list(unique_items.values())


if __name__ == "__main__":
    categories = [  # Our 24 chosen categories.
        "civil_softwares", "tutorials", "confidential_info", "cards_and_cvv",
        "hacks", "application_software", "accounts", "documents",
        "false_documents", "exploit_kit", "drop_bank", "security",
        "system_software", "utilities", "software_forensics_tools", "forgery",
        "network_services", "database", "leaked_documents", "digital_forensics",
        "0day", "intelligence", "private_security", "racketeering"
    ]

    results_directory = "./categoryPageTitleStats/"
    os.makedirs(results_directory, exist_ok=True)

    for category in categories:
        directory = f"./new_onion_sites_html/{category}/"
        items = extract_category_page(directory)

        csv_filepath = os.path.join(results_directory,
                                    f"{category}.csv")
        if not os.path.exists(csv_filepath):
            try:
                with open(csv_filepath, 'w', newline='', encoding='utf-8') as file:
                    writer = csv.writer(file)
                    writer.writerow(['Title', 'Stats'])
                    writer.writerows(items)
                print(f"CSV file for {category} created successfully.")
            except Exception as e:
                print(f"Error creating CSV file for {category}: {e}")
        else:
            print(f"CSV file for {category} has already been created.")

    print("All CSV-files have been created successfully.")
