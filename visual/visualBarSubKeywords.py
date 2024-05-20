import matplotlib.pyplot as plt

# Data
categories = ['Malware', 'Phishing', 'Hacking', 'Course']
frequencies = [1896, 770, 612, 5282]

# Create bar chart
plt.figure(figsize=(10, 6))
bars = plt.bar(categories, frequencies, color=['blue', 'orange', 'green', 'red'])

# Add numbers on top of bars
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 50, int(yval), ha='center', va='bottom')

# Add titles and labels
plt.title('Frequency of Access Crime')
plt.xlabel('Subcategories')
plt.ylabel('Frequency')

# Display the chart
plt.show()
