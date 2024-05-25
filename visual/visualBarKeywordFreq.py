import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("merged_data.csv")
keywords = ['malware', 'trojan', 'ransomware', 'rat', 'keylogger', 'spyware', 'worm']

""" Function keyword_search() searches each keyword for both singular and plural, by adding
an s to each word. One word in singular and plural are merged together. This to give better accuracy. 
"""

""" The rest of the code finds the keywords in the CSV-file, counts them and displays occurences in each element
but also their total occurences in both elements. 
"""


def keyword_search(keyword, column):
    count_singular = df[column].str.contains(keyword, case=False, na=False).sum()
    plural_keyword = keyword + 's'
    count_plural = df[column].str.contains(plural_keyword, case=False, na=False).sum()
    return count_singular + count_plural


title_keyword_counts = {key: 0 for key in keywords}
description_keyword_counts = {key: 0 for key in keywords}

for keyword in keywords:
    title_keyword_counts[keyword] = keyword_search(keyword, 'Heading')

for keyword in keywords:
    description_keyword_counts[keyword] = keyword_search(keyword, 'Tab1')

title_keyword_df = pd.DataFrame(list(title_keyword_counts.items()), columns=['Keyword', 'Title_Count'])
description_keyword_df = pd.DataFrame(list(description_keyword_counts.items()),
                                      columns=['Keyword', 'Description_Count'])
merged_keyword_df = pd.merge(title_keyword_df, description_keyword_df, on='Keyword')
merged_keyword_df['Total_Count'] = merged_keyword_df['Title_Count'] + merged_keyword_df['Description_Count']
total_sum = merged_keyword_df['Total_Count'].sum()
total_row = pd.DataFrame([['Total', 0, 0, total_sum]],
                         columns=['Keyword', 'Title_Count', 'Description_Count', 'Total_Count'])
merged_keyword_df = pd.concat([merged_keyword_df, total_row], ignore_index=True)
print(merged_keyword_df)

ax = merged_keyword_df.plot(kind='bar', x='Keyword', y=['Title_Count', 'Description_Count', 'Total_Count'],
                            title='Keyword Frequency in Titles and Descriptions for Network Attacks', figsize=(10, 6))
ax.set_xlabel("Keyword")
ax.set_ylabel("Frequency")

for pos, row in merged_keyword_df.iterrows():
    ax.text(pos - 0.25, row['Title_Count'] + 0.5, str(row['Title_Count']), ha='center', va='bottom', fontsize=8)
    ax.text(pos, row['Description_Count'] + 0.5, str(row['Description_Count']), ha='center', va='bottom', fontsize=8)
    ax.text(pos + 0.25, row['Total_Count'] + 0.5, str(row['Total_Count']), ha='center', va='bottom', fontsize=8)

plt.xticks(rotation=45, ha='right')

plt.tight_layout()
plt.show()
