import matplotlib.pyplot as plt

# Define the data
categories = ['DDoS']
keyword_counts = [
    {'DDoS': 39}
]

# Extracting keywords and frequencies
keywords = []
frequencies = []
for item in keyword_counts:
    keyword, frequency = list(item.items())[0]
    keywords.append(keyword)
    frequencies.append(frequency)

# Create bar plot
plt.figure(figsize=(10, 6))
bars = plt.bar(categories, frequencies, color=['red', 'blue', 'green', 'orange'])

# Add labels and title
plt.xlabel('Categories')
plt.ylabel('Counts')
plt.title('Number of Mentions in Network Crime')

# Add count annotations
for i, rect in enumerate(bars):
    height = rect.get_height()
    plt.annotate('{}'.format(height),
                 xy=(rect.get_x() + rect.get_width() / 2, height),
                 xytext=(0, 3),  # 3 points vertical offset
                 textcoords="offset points",
                 ha='center', va='bottom')

# Show plot
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
