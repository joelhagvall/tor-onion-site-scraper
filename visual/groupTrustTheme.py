import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Function to count occurrences of specified themes and keywords in each row of a column
def count_occurrences(df, column_name, themes):
    theme_counts = {theme: 0 for theme in themes}
    keyword_counts = {theme: {keyword: 0 for keyword in themes[theme]} for theme in themes}
    for index, row in df.iterrows():
        if pd.notna(row[column_name]):
            elements = row[column_name].split(',')
            for element in elements:
                word = element.strip()
                for theme in themes:
                    if word in themes[theme]:
                        theme_counts[theme] += 1
                        keyword_counts[theme][word] += 1
    return theme_counts, keyword_counts

# Read the CSV file
file_path = 'trustListings.csv'  # Replace with your actual file path
df = pd.read_csv(file_path)

# Specify the column name you want to analyze
column_to_analyze = 'Trust Theme'

# Define the 5 trust themes and their respective themes
trust_themes = {
    'Customer Care and Reviews': ['Assistance', 'Friendly','Appreciation from buyer', 'Appreciation from seller', 
                                  'Criticism'],
    'Product and Service Quality': ['Delivery', 'Quality', 'Extensive Description', 'Authenticity', 'Exaggerated Claims',
                                    'Transparency', 'Reliability', 'Efficiency'],
    'Security': ['Security', 'Anonymity', 'Disclaimer'],
    'Value and Assurance': ['Rewards', 'Value', 'Assurance', 'Financial Gain', 'Pricing Strategy', 'Customization', 
                            'Tutorials', 'Advisory', 'Credibility', 'Success', 'Success Stories', 'Warranty', 'Satisfaction Guarantee', 
                                    'Refund', 'Problem Guarantee', 'Guarantee'],
    'Ethics and Compliance': ['Ethical Considerations', 'Responsibility']
}

# Count occurrences of specified themes and keywords in the specified column
theme_counts, keyword_counts = count_occurrences(df, column_to_analyze, trust_themes)

# Sort the themes based on their counts in descending order
sorted_themes = sorted(theme_counts.items(), key=lambda x: x[1], reverse=True)

# Prepare data for plotting
themes = [theme for theme, count in sorted_themes]
counts = [count for theme, count in sorted_themes]

# Generate a color palette
unique_colors = sns.color_palette("husl", len(themes))

# Plotting the main bar chart for themes
plt.figure(figsize=(14, 10))

# Main plot for themes
plt.subplot(2, 1, 1)
bars = plt.bar(themes, counts, color=unique_colors)
for bar, count in zip(bars, counts):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), str(count), ha='center', va='bottom')
plt.title('Trust Themes Count in 200 Listings')
plt.xlabel('Trust Themes')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Subplot for keyword occurrences (for top 5 themes)
plt.subplot(2, 1, 2)
for i, theme in enumerate(themes):
    keywords = list(keyword_counts[theme].keys())
    keyword_occurrences = list(keyword_counts[theme].values())
    sorted_keywords = sorted(zip(keyword_occurrences, keywords), reverse=True)[:10]  # Select top 10 keywords per theme
    sorted_keyword_occurrences = [occurrence for occurrence, keyword in sorted_keywords]
    sorted_keywords = [keyword for occurrence, keyword in sorted_keywords]
    bars = plt.bar(sorted_keywords, sorted_keyword_occurrences, color=[unique_colors[i]] * len(sorted_keywords), label=theme)
    for bar, count in zip(bars, sorted_keyword_occurrences):
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), str(count), ha='center', va='bottom')

plt.title('Keyword Occurrences by Top 5 Themes')
plt.xlabel('Keywords')
plt.ylabel('Occurrences')
plt.xticks(rotation=90)
plt.legend(loc='upper right', bbox_to_anchor=(1.15, 1), title='Themes')
plt.tight_layout()

# Display the plot
plt.show()
