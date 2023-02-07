import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Task 1: Read CSV file and transfer it into DataFrame
df = pd.read_csv("data.csv", sep=";")

# Task 2: Transfer object Series into index column of the dataframe
df.set_index('quality', inplace=True)

# Task 3: Change the data in the column of DataFrame according to some condition
df['alcohol'] = df['alcohol'].apply(lambda x: x + 1 if x >= 10 else x)

# Task 4: Get names of the DataFrame columns and sum of losted values DF
cols = df.columns
missing_values = df.isnull().sum().sum()
print("Columns: ", cols)
print("Missing Values: ", missing_values)

# Task 5: Exchange 2 columns, use function for it. Sort coulumn by name
df[['alcohol', 'citric acid']] = df[['citric acid', 'alcohol']]
df.sort_index(axis=1, ascending=True, inplace=True)

# Task 6: Delete upper and lowe 5% in object DataFrame
q1 = df.quantile(0.05)
q2 = df.quantile(0.95)
df = df[(df > q1) & (df < q2)].dropna()

# Task 7: Replay ( Apply) missed values in the Column with average values.
df.fillna(df.mean(), inplace=True)

# Task 8: Create two data frames using the two Dicts, Merge two data frames, and append the second data frame as a new column to the first data frame.
dict1 = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}
dict2 = {'A': [10, 20, 30], 'B': [40, 50, 60], 'C': [70, 80, 90]}
df1 = pd.DataFrame(dict1)
df2 = pd.DataFrame(dict2)
merged_df = pd.merge(df1, df2, on='A')
df1['D'] = df2['C']

# Task 9: For any column create histogram
df['alcohol'].plot(kind='hist')
plt.show()

# Task 10: Create Correlation Matrix for any column
corr = df.corr()
print(corr)
