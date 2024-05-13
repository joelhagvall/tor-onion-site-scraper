import os
import csv
from bs4 import BeautifulSoup

def extract_from_html_files(directory):
    unique_items = []  # Use a list to store unique items
    
    # Iterate through all files in the directory
    for filename in os.listdir(directory):
        if "1_category_drugs_production" in filename:
            continue  # Skip the specified file
        if "category" in filename:
            continue  # Skip files that contain "category" in their names
        if "product" not in filename:
            continue  # Skip files that don't contain "product" in their names
        
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):  # Check if it's a file
            with open(filepath, "r", encoding="utf-8") as file:
                html_content = file.read()
                soup = BeautifulSoup(html_content, 'html.parser')

                # Extract title and description if they are found only once per file
                title_content = soup.find('div', class_='title')
                description_content = soup.find('div', class_='description')
                
                if title_content and description_content:
                    title_text = title_content.text.strip()
                    description_text = description_content.text.strip()
                    unique_items.append([title_text, description_text])
    
    return unique_items

if __name__ == "__main__":
    category = "accounts"  # Define the category name
    directory = f"./new_onion_sites_html/{category}/"  # Use f-string to make the category name dynamic
    items = extract_from_html_files(directory)

    # Save extracted data to CSV in the "results" directory
    results_directory = "./resultsHTML/"
    os.makedirs(results_directory, exist_ok=True)  # Create the directory if it doesn't exist
    csv_filepath = os.path.join(results_directory, f"{category}.csv")  # Use f-string to make the CSV filename dynamic
    with open(csv_filepath, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'Description'])
        writer.writerows(items)
    
    print(f"Total unique items extracted from HTML files: {len(items)}")
