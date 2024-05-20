import pandas as pd
import os

# Directory containing your CSV files
results_directory = 'productPageResultsHTML'

# List all CSV files in the resultsHTML directory
results_csv_files = [file for file in os.listdir(results_directory) if file.endswith('.csv')]

# Initialize an empty list to store DataFrame objects
dfs = []

# Loop through each CSV file in the resultsHTML directory, read it into a DataFrame, and append it to the list
for file in results_csv_files:
    file_path = os.path.join(results_directory, file)
    df = pd.read_csv(file_path)
    dfs.append(df)

# Concatenate all DataFrames in the list along the rows
merged_df = pd.concat(dfs, ignore_index=True)

# Now merged_df contains the merged data from all CSV files within the resultsHTML directory
# You can then save this merged DataFrame to a new CSV file if needed
merged_df.to_csv('merged_data.csv', index=False)
