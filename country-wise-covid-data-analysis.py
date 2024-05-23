import pandas as pd 
import numpy as np

# Problem 1: Load the Data

df = pd.read_csv("country_wise_latest.csv")
print(df)

# problem 2: Statistical Analysis
# Calculate the mean and standard deviation for the Confirmed, Deaths, Recovered, and Active columns.
print(df.head(10))

confirmed_mean = df['Confirmed'].mean()
print("confirmed_mean",confirmed_mean)
confirmed_std = df['Confirmed'].std()
print("confirmed_std",confirmed_std)


Deaths_mean = df['Deaths'].mean()
print("Deaths_mean",Deaths_mean)
Deaths_std = df['Deaths'].std()
print("Deaths_std",Deaths_std)

Active_mean = df['Active'].mean()
print("Active_mean",Active_mean)
Active_std = df['Active'].std()
print("Active_std",Active_std)

Recovered_mean = df['Recovered'].mean()
print("Recovered_mean",Recovered_mean)
Recovered_std = df['Recovered'].std()
print("Recovered_std",Recovered_std)

### Problem 3: Filter and Sort
# Filter the data to show only countries with more than 100,000 confirmed cases and sort them by the number of confirmed cases in descending order.


filtered_sorted_df = df[df["Confirmed"]>10000].sort_values("Confirmed",ascending=False)
print("filtered_sorted_df",filtered_sorted_df)

# Problem 4: New Cases and Deaths per Region
# Calculate the total new cases and new deaths per WHO region
print(df.columns)

total_new_cases_per_region = df.groupby("WHO Region")["New cases"].sum()
print(total_new_cases_per_region)
total_new_Deaths_per_region = df.groupby("WHO Region")["New deaths"].sum()
print(total_new_Deaths_per_region)

#  Problem 5: Case Fatality Rate
# Calculate the case fatality rate (deaths per 100 confirmed cases) for each country and add it as a new column.


df["case fatality rate"] = (df['Deaths'] / df['Confirmed']) * 100
print(df)

# Problem 6: Top 5 Countries by Active Cases
# Find the top 5 countries with the highest number of active cases.
top_5_active_cases = df.sort_values("Active",ascending=False).head()
print(top_5_active_cases)
print(df['Active'])

print(top_5_active_cases['Active'])

