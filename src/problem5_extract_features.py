"""
Problem 5: Extracting the required data
---------------------------------------
Goal: Practice pulling out subsets of data from the DataFrame.

Tasks:
1. Extract the sepal_width column in two ways.
2. Extract rows 50-99.
3. Extract rows 50-99 of only petal_length.
4. Extract rows where petal_width == 0.2.
5. Explain .loc vs .iloc differences.
Also: Save each extracted subset as a CSV in the data/ folder.
"""

import pandas as pd
import os

# Ensure data folder exists
os.makedirs("data", exist_ok=True)

# Load the combined DataFrame from problem 2
df = pd.read_csv("data/iris_combined.csv")

print("=== Problem 5: Extracting Features ===")

# 1. Extract sepal_width column in two ways
sepal_width_method1 = df['sepal_width']
sepal_width_method2 = df.loc[:, 'sepal_width']

print("\n1. Extract sepal_width column in two ways:")
print("Using df['sepal_width']:\n", sepal_width_method1.head())
print("Using df.loc[:, 'sepal_width']:\n", sepal_width_method2.head())

# Save to CSV
sepal_width_method1.to_csv("data/subset_sepal_width_method1.csv", index=False)
sepal_width_method2.to_csv("data/subset_sepal_width_method2.csv", index=False)

# 2. Extract rows 50–99
rows_50_99 = df.iloc[50:100]   # 100 not included
print("\n2. Extract rows 50-99:")
print(rows_50_99)
rows_50_99.to_csv("data/subset_rows_50_99.csv", index=False)

# 3. Extract rows 50–99 of only petal_length
petal_length_50_99 = df.loc[50:99, ['petal_length']]
print("\n3. Extract rows 50-99 of only petal_length:")
print(petal_length_50_99)
petal_length_50_99.to_csv("data/subset_petal_length_50_99.csv", index=False)

# 4. Extract rows where petal_width == 0.2
petal_width_eq_02 = df[df['petal_width'] == 0.2]
print("\n4. Extract rows where petal_width == 0.2:")
print(petal_width_eq_02)
petal_width_eq_02.to_csv("data/subset_petal_width_eq_02.csv", index=False)

# 5. Explanation of loc vs iloc
print("\n5. Difference between .loc and .iloc:")
print(".loc -> label-based indexing (uses row/column names).")
print(".iloc -> position-based indexing (uses row/column numbers).")

print("\n Problem 5 complete. Subsets saved to data/ folder.")
