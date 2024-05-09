import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the CSV file
df = pd.read_csv("merged_data.csv")


# Step 2: Define the keywords
keywords = ['malware', 'trojan', 'ransomware', 'spyware', 'keylogger']

# Step 3: Initialize a dictionary to store counts
keyword_counts = {key: 0 for key in keywords}

# Step 4: Count the occurrences in the title
for keyword in keywords:
    # case insensitive searching
    keyword_counts[keyword] += df['Description'].str.contains(keyword, case=False, na=False).sum()

# Step 5: Convert the counts to a DataFrame for easier handling
keyword_df = pd.DataFrame(list(keyword_counts.items()), columns=['Keyword', 'Count'])

# Step 6: Display the DataFrame
print(keyword_df)

# Step 7: Plot the data
ax = keyword_df.plot(kind='bar', x='Keyword', y='Count', title='Keyword Frequency in Descriptions')

# Step 8: Annotate each bar with its count
for index, row in keyword_df.iterrows():
    ax.text(index, row['Count'], str(row['Count']), ha='center', va='bottom')

plt.show()
