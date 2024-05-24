import pandas as pd 
import numpy as np

df = pd.read_csv("student_addiction_dataset_test.csv")
print(df)

# Fill missing values with 'Unknown'
df.fillna("unknown", inplace=True)

df_column =df.columns.str.replace("_"," ")
print(df_column)

for column in df.columns:
    df[column] = df[column].astype(str)

#  the percentage of each category in the Addiction_Class column
class_percentage = df['Addiction_Class'].value_counts(normalize=True) * 100
print("Percentage of each category in Addiction_Class column:")
print(class_percentage)


# statistics summary for each column
summary_stats = df.describe()
print("\nSummary statistics for each column:")
print(summary_stats)

df.replace({"Yes":1,"No":0},inplace=True)
#  a new column that counts the number of "Yes" responses for each row
df['Yes_Count'] = (df == 1).sum(axis=1)

# Calculate  correlation matrix
correlation_matrix = df.corr()
print("\nCorrelation Matrix:")
print(correlation_matrix)

print(df)


