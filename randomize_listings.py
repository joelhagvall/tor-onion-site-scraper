import pandas as pd

# Step 1: Read the CSV file into a DataFrame
input_file = 'merged_data.csv'  # Replace with your input file path
df = pd.read_csv(input_file)

# Step 2: Randomize the rows and select 200 of them
df_randomized = df.sample(n=200, random_state=1)  # random_state for reproducibility

# Step 3: Write the randomized rows to a new CSV file
output_file = 'random_listings.csv'  # Replace with your desired output file path
df_randomized.to_csv(output_file, index=False)
