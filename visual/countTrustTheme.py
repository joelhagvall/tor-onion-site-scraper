import csv
from collections import Counter

def count_words_in_column(csv_file, column_name):
    word_counter = Counter()
    
    with open(csv_file, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if column_name in row:
                words = row[column_name].split(',')
                for word in words:
                    word = word.strip()  # Remove any leading/trailing whitespace
                    if word:  # Ensure the word is not empty
                        word_counter[word] += 1
    
    return word_counter

def display_word_counts_table(word_counts):
    sorted_word_counts = dict(sorted(word_counts.items(), key=lambda item: item[1], reverse=True))
    
    print(f"{'Word/Phrase':<20} {'Count':<5}")
    print("-" * 25)
    for word, count in sorted_word_counts.items():
        print(f"{word:<20} {count:<5}")

# Specify the CSV file path and the column name
csv_file_path = 'trustListings.csv'
column_name = 'Trust Theme'

# Count the words in the specified column
word_counts = count_words_in_column(csv_file_path, column_name)

# Display the word counts as a table
display_word_counts_table(word_counts)
