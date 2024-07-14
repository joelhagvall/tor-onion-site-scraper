import pandas as pd

input_file = 'merged_data.csv'  # Replace with your input file path
df = pd.read_csv(input_file)

df_randomized = df.sample(n=200, random_state=1)  # random_state for reproducibility

output_file = 'random_listings.csv'  # Replace with your desired output file path
df_randomized.to_csv(output_file, index=False)
