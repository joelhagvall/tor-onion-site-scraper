import csv
import os
from bs4 import BeautifulSoup

def extract_data(html_file, column_names):
    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()

    soup = BeautifulSoup(html_content, 'html.parser')

    data = []
    for item in soup.select('.item'):
        title = item.select_one('.title').get_text(strip=True)
        description = item.select_one('.description').get_text(strip=True)
        price = item.select_one('.price').get_text(strip=True)

        row = [title, description, price]
        data.append(row)

    return data

def save_to_csv(data, file_name, column_names):
    full_path = os.path.join(os.getcwd(), file_name)  # Path to save file in current directory
    with open(full_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(column_names)
        writer.writerows(data)

if __name__ == '__main__':
    html_file = input("Enter the HTML file path: ")
    column_names = input("Enter the column names (separated by commas): ").split(',')

    data = extract_data(html_file, column_names)
    csv_file_name = input("Enter the output CSV file name: ")  # Ask for file name only

    save_to_csv(data, csv_file_name, column_names)
    print(f"CSV file '{csv_file_name}' has been created successfully in the current directory!")
