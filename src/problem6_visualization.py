"""
Problem 6: Creating diagrams (visualization)
--------------------------------------------
Goal: Visualize data distributions.

Tasks:
1. Pie chart of sample counts per label (with percentages).
2. Box plot of each feature per species.
3. Violin plot of each feature per species.
Also: Save plots to plots/ folder instead of displaying (since we use GitBash).
"""

import matplotlib
matplotlib.use("Agg")   # prevents GUI issues in GitBash
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

# Ensure plots folder exists
os.makedirs("plots", exist_ok=True)

# Load the combined iris DataFrame
df = pd.read_csv("data/iris_combined.csv")

print("=== Problem 6: Data Visualization ===")

# 1. Pie chart of sample counts per label
species_counts = df['Species'].value_counts()
plt.figure(figsize=(6,6))
plt.pie(
    species_counts,
    labels=species_counts.index,
    autopct='%1.1f%%',
    startangle=90,
    colors=['#ff9999','#66b3ff','#99ff99']
)
plt.title("Sample Counts per Species (Pie Chart)")
plt.savefig("plots/problem6_pie_chart.png")
plt.close()
print("Saved: plots/problem6_pie_chart.png")

# 2. Box plot for each feature per species
for feature in ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']:
    plt.figure(figsize=(8,6))
    sns.boxplot(x="Species", y=feature, data=df)
    plt.title(f"Box Plot of {feature} by Species")
    plt.savefig(f"plots/problem6_boxplot_{feature}.png")
    plt.close()
    print(f"Saved: plots/problem6_boxplot_{feature}.png")

# 3. Violin plot for each feature per species
for feature in ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']:
    plt.figure(figsize=(8,6))
    sns.violinplot(x="Species", y=feature, data=df, inner="quartile")
    plt.title(f"Violin Plot of {feature} by Species")
    plt.savefig(f"plots/problem6_violin_{feature}.png")
    plt.close()
    print(f"Saved: plots/problem6_violin_{feature}.png")

# Explanation of box vs violin plots
print("\n=== Explanation ===")
print("Box plot: shows median, quartiles (Q1, Q3), and potential outliers.")
print("Violin plot: combines a box plot with a kernel density estimate,")
print("             so it shows both quartiles and the distribution shape.")

print("\n Problem 6 complete. All plots saved in plots/ folder.")
