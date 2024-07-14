import pandas as pd
import matplotlib.pyplot as plt

# Function to count occurrences of specified themes in each row of a column
def count_occurrences(df, column_name, themes):
    theme_counts = {theme: 0 for theme in themes}
    for index, row in df.iterrows():
        if pd.notna(row[column_name]):
            elements = row[column_name].split(',')
            for element in elements:
                word = element.strip()
                if word in theme_counts:
                    theme_counts[word] += 1
    return theme_counts

# Read the CSV file
file_path = 'trustListings.csv'  # Replace with your actual file path
df = pd.read_csv(file_path)

# Specify the column name you want to analyze
column_to_analyze = 'Trust Theme'

# Specify the themes you want to search for
themes_to_search = ['Assistance', 'Security']

# Count occurrences of specified themes in the specified column
theme_counts = count_occurrences(df, column_to_analyze, themes_to_search)

# Prepare data for plotting
themes = list(theme_counts.keys())
counts = list(theme_counts.values())

# Define a list of colors for the bars
colors = ['skyblue', 'lightgreen', 'lightcoral', 'lightpink', 'lightseagreen']

# Ensure the number of colors matches the number of themes
if len(colors) < len(themes):
    colors = colors * (len(themes) // len(colors)) + colors[:len(themes) % len(colors)]

# Plotting the bar chart
plt.figure(figsize=(10, 6))
bars = plt.bar(themes, counts, color=colors[:len(themes)])

# Adding counts above the bars
for bar, count in zip(bars, counts):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), str(count), ha='center', va='bottom')

plt.title('Specified Trust Themes Count in 200 Listings')
plt.xlabel('Trust Themes')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Display the plot
plt.show()
