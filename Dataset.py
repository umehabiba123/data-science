import pandas as pd
import numpy as np

file_name = 'heart.csv'
df = pd.read_csv(file_name)
print(df)
print(df.describe())
filtered_df = df[(df['age'] > 50) & (df['target'] == 1)]
print(filtered_df)

# Mean of each column
mean_values = df.mean()
print(mean_values)


# Group by 'sex' and calculate the mean for each group
grouped_df = df.groupby('sex').mean()
print(grouped_df)

# Create a new column 'age_category' based on age
df['age_category'] = pd.cut(df['age'], bins=[0, 30, 50, 70, 100], labels=['0-30', '31-50', '51-70', '71-100'])
print(df.head())

