import matplotlib.pyplot as plt


""" Script that based on categories and frequencies entered, displays the categories and their
frequencies using bars in different colors.
"""

categories = ['Leaks', 'Database', 'Credit Card', 'Account']
frequencies = [306, 383, 2799, 3781]

plt.figure(figsize=(10, 6))
bars = plt.bar(categories, frequencies, color=['blue', 'orange', 'green', 'red'])

for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, str(int(yval)), ha='center', va='bottom')

plt.title('Frequency of Data Crime')
plt.xlabel('Subcategories')
plt.ylabel('Frequency')
plt.show()
