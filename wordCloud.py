import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Read CSV file
df = pd.read_csv('results/1. civil_softwares.csv')

# Concatenate text data
text = ' '.join(df['Title'])  # Change 'column1' to your desired column name

# Generate word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

# Display the word cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
