import pandas as pd
import os


""" This script merges all CSV-files found in the specified directory of the results_directory-variable.
    It finds every column and row and concatenates these to the same CSV-file.
"""

results_directory = 'categoryPageTitleStats'
results_csv_files = [file for file in os.listdir(results_directory) if file.endswith('.csv')]

dfs = []

for file in results_csv_files:
    file_path = os.path.join(results_directory, file)
    df = pd.read_csv(file_path)
    dfs.append(df)

merged_df = pd.concat(dfs, ignore_index=True)
merged_df.to_csv('categoryTitleStats.csv', index=False)
