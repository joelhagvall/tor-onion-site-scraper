import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the CSV file
df = pd.read_csv('merged_data.csv')

# Step 2: Define the keywords
keywords = ['malware', 'leaks', 'data leaks', 'database', 'credit card', 'carding', 'password',
            'account', 'malware', 'ransomware', 'phishing', 'hacking', 'ddos', 'virus', 'course', 'worms']

# Step 3: Initialize a dictionary to store counts
keyword_counts = {key: 0 for key in keywords}

# Step 4: Count the occurrences in both the title and description
for keyword in keywords:
    # Case insensitive searching
    keyword_counts[keyword] += df['Title'].str.contains(keyword, case=False, na=False).sum()
    keyword_counts[keyword] += df['Description'].str.contains(keyword, case=False, na=False).sum()

# Step 5: Convert the counts to a DataFrame for easier handling
keyword_df = pd.DataFrame(list(keyword_counts.items()), columns=['Keyword', 'Count'])

# Step 6: Display the DataFrame
print(keyword_df)

# Step 7: Plot the data as a pie chart
plt.figure(figsize=(8, 8))  # Set the figure size
plt.pie(keyword_df['Count'], labels=keyword_df['Keyword'],
        autopct=lambda p: '{:.1f}%\n({:.0f})'.format(p, (p / 100) * keyword_df['Count'].sum()), startangle=140)
plt.title('Keyword Frequency in Listings')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()
