from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

# Read HTML content from file
with open('index.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Find all categories and their frequencies
categories = {}
for category_div in soup.find_all('label', class_='category'):
    category_name = category_div.text.strip()
    category_count = int(category_div['title'].split('(')[1].split(')')[0])
    categories[category_name] = category_count

# Plotting
plt.figure(figsize=(12, 8))

categories_names = list(categories.keys())
categories_counts = list(categories.values())

plt.bar(categories_names, categories_counts, color='skyblue')

plt.xlabel('Categories')
plt.ylabel('Frequency')
plt.title('Frequency of Categories')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

plt.show()
