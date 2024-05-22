import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the CSV file
df = pd.read_csv("merged_data.csv")

# Step 2: Define the keywords
keywords = ['attacks', 'wi-fi cracking', 'rogue access points', 'firewall']

# Function to search for both singular and plural forms of a keyword
def search_keyword(keyword, column):
    count_singular = df[column].str.contains(keyword, case=False, na=False).sum()
    plural_keyword = keyword + 's'
    count_plural = df[column].str.contains(plural_keyword, case=False, na=False).sum()
    return count_singular + count_plural

# Step 3: Initialize dictionaries to store counts for title and description
title_keyword_counts = {key: 0 for key in keywords}
description_keyword_counts = {key: 0 for key in keywords}

# Step 4: Count the occurrences in the title
for keyword in keywords:
    title_keyword_counts[keyword] = search_keyword(keyword, 'Heading')

# Step 5: Count the occurrences in the description
for keyword in keywords:
    description_keyword_counts[keyword] = search_keyword(keyword, 'Tab1')

# Step 6: Convert the counts to DataFrames for easier handling
title_keyword_df = pd.DataFrame(list(title_keyword_counts.items()), columns=['Keyword', 'Title_Count'])
description_keyword_df = pd.DataFrame(list(description_keyword_counts.items()), columns=['Keyword', 'Description_Count'])

# Step 7: Merge the DataFrames on the 'Keyword' column
merged_keyword_df = pd.merge(title_keyword_df, description_keyword_df, on='Keyword')

# Step 8: Calculate the sum of frequencies
merged_keyword_df['Total_Count'] = merged_keyword_df['Title_Count'] + merged_keyword_df['Description_Count']

# Step 9: Calculate the sum for all total keywords together
total_sum = merged_keyword_df['Total_Count'].sum()

# Step 10: Add the sum of all total keywords as a new row to the DataFrame
total_row = pd.DataFrame([['Total', 0, 0, total_sum]], columns=['Keyword', 'Title_Count', 'Description_Count', 'Total_Count'])
merged_keyword_df = pd.concat([merged_keyword_df, total_row], ignore_index=True)

# Step 11: Display the DataFrame
print(merged_keyword_df)

""" colors = ['#555555', '#AAAAAA', '#DDDDDD']  # dark gray, medium gray, light gray """

# Step 12: Plot the data
ax = merged_keyword_df.plot(kind='bar', x='Keyword', y=['Title_Count', 'Description_Count', 'Total_Count'], 
                            title='Keyword Frequency in Titles and Descriptions for Network Attacks', figsize=(10, 6))

# Step 13: Set axis labels
ax.set_xlabel("Keyword")
ax.set_ylabel("Frequency")

# Step 14: Annotate each bar with its count
for index, row in merged_keyword_df.iterrows():
    ax.text(index - 0.25, row['Title_Count'] + 0.5, str(row['Title_Count']), ha='center', va='bottom', fontsize=8)
    ax.text(index, row['Description_Count'] + 0.5, str(row['Description_Count']), ha='center', va='bottom', fontsize=8)
    ax.text(index + 0.25, row['Total_Count'] + 0.5, str(row['Total_Count']), ha='center', va='bottom', fontsize=8)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha='right')

plt.tight_layout()
plt.show()
