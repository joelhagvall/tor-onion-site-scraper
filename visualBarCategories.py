from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

# Load HTML content from file
with open("index.html", "r", encoding="utf-8") as file:
    html_content = file.read()

# Parse HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Find category labels and their quantities
categories = soup.find_all('label', class_='category')
quantities = [int(category.text.split('(')[-1].split(')')[0]) for category in categories]

# Find category names
category_names = [category.text.split('(')[0].strip() for category in categories]

# Sort categories and quantities in descending order of quantity
sorted_categories, sorted_quantities = zip(*sorted(zip(category_names, quantities), key=lambda x: x[1], reverse=True))

# Plot bar chart
plt.figure(figsize=(12, 8))
plt.barh(sorted_categories, sorted_quantities, color='skyblue')
plt.xlabel('Quantities')
plt.ylabel('Categories')
plt.title('Categories and their Quantities')
plt.gca().invert_yaxis()  # Invert y-axis to display categories from top to bottom
for index, value in enumerate(sorted_quantities):
    plt.text(value, index, str(value))
plt.show()
