import pandas as pd
import matplotlib.pyplot as plt

# Function to count occurrences of words in each row of a column
def count_occurrences(df, column_name):
    word_counts = {}
    for index, row in df.iterrows():
        if pd.notna(row[column_name]):
            elements = row[column_name].split(',')
            for element in elements:
                word = element.strip()
                if word in word_counts:
                    word_counts[word] += 1
                else:
                    word_counts[word] = 1
    return word_counts

# Read the CSV file
file_path = 'trustListings.csv'  # Replace with your actual file path
df = pd.read_csv(file_path)

# Specify the column name you want to analyze
column_to_analyze = 'Trust Theme'

# Count occurrences of words in the specified column
word_counts = count_occurrences(df, column_to_analyze)

# Prepare data for plotting
words = list(word_counts.keys())
counts = list(word_counts.values())

# Plotting the bar chart
plt.figure(figsize=(10, 6))
plt.bar(words, counts, color='skyblue')
plt.title('Trust Elements Count in 200 Listings')
plt.xlabel('Trust Elements')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Display the plot
plt.show()
