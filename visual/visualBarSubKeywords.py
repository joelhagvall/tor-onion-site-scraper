import matplotlib.pyplot as plt

# Data
categories = ['Malware', 'Phishing', 'Hacking', 'Course']
frequencies = [1896, 770, 612, 5282]

# Create bar chart
plt.figure(figsize=(10, 6))
plt.bar(categories, frequencies, color=['blue', 'orange', 'green', 'red'])

# Add titles and labels
plt.title('Frequency of Access Crime')
plt.xlabel('Categories')
plt.ylabel('Frequency')

# Display the chart
plt.show()
