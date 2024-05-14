import os
import csv
from bs4 import BeautifulSoup

def extract_from_html_files(directory):
    unique_items = {}  # Use a dictionary to store unique items
    
    # Iterate through all files in the directory
    for filename in os.listdir(directory):
        if filename != "1_category_drugs_production.html":
            if "category" in filename:
                pass
            else:
                continue  # Skip files that don't contain "category" in their names

            filepath = os.path.join(directory, filename)
            if not os.path.isfile(filepath):  # Check if it's a file
                continue
            with open(filepath, "r", encoding="utf-8") as file:
                html_content = file.read()
                soup = BeautifulSoup(html_content, 'html.parser')

                # Extract title and description from each item on the page
                for item in soup.find_all('div', class_='item'):
                    title = item.find('div', class_='title').text.strip() if item.find('div',
                                                                                       class_='title') else 'No Title'
                    description = item.find('div', class_='description').text.strip() if item.find('div',
                                                                                                   class_='description') else 'No Description'
                    unique_key = f"{title}|{description}"  # Create a unique key for each item
                    if unique_key in unique_items:
                        continue
                    unique_items[unique_key] = [title, description]

    return list(unique_items.values())  # Convert the dictionary values to a list

if __name__ == "__main__":
    category = "civil_softwares"  # Define the category name
    directory = f"./new_onion_sites_html/{category}/"  # Use f-string to make the category name dynamic
    items = extract_from_html_files(directory)

    # Save extracted data to CSV in the "resultsHTML" directory
    results_directory = "./resultsHTML/"
    os.makedirs(results_directory, exist_ok=True)  # Create the directory if it doesn't exist
    
    csv_filepath = os.path.join(results_directory, f"{category}.csv")  # Use f-string to make the CSV filename dynamic
    with open(csv_filepath, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'Description'])
        writer.writerows(items)
    
    print(f"Total unique items extracted from HTML files: {len(items)}")
