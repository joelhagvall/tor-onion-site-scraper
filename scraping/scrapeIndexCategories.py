from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

# Read HTML content from file
with open('index.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Find all categories and their subcategories
categories = {}
for category_div in soup.find_all('label', class_='category'):
    category_name = category_div.text.strip()
    subcategories = []
    for subcat_link in category_div.find_next_siblings('a'):
        subcategory_name = subcat_link.text.strip().split('(')[0].strip()
        subcategory_count = int(subcat_link.text.strip().split('(')[1].split(')')[0])
        subcategories.append((subcategory_name, subcategory_count))
    categories[category_name] = subcategories

# Plotting
plt.figure(figsize=(10, 8))
for category, subcategories in categories.items():
    sizes = [sub[1] for sub in subcategories]
    labels = [sub[0] for sub in subcategories]
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title(category)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.show()
