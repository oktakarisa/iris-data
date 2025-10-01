import matplotlib
matplotlib.use("Agg")  # prevent display issues in GitBash

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os


def main():
    # Ensure plots folder exists
    os.makedirs("plots", exist_ok=True)

    # Load combined dataset
    df = pd.read_csv("data/iris_combined.csv")

    print("\n Problem 7: Feature Relationships")

    # Define feature pairs
    pairs = [
        ("sepal_length", "sepal_width"),
        ("sepal_length", "petal_length"),
        ("sepal_length", "petal_width"),
        ("sepal_width", "petal_length"),
        ("sepal_width", "petal_width"),
        ("petal_length", "petal_width"),
    ]

    # Scatter plots
    for x, y in pairs:
        plt.figure(figsize=(6, 4))
        sns.scatterplot(x=x, y=y, hue="Species", data=df)
        plt.title(f"{x} vs {y}")
        fname = f"plots/problem7_scatter_{x}_{y}.png"
        plt.savefig(fname)
        plt.close()

    # Pairplot
    sns.pairplot(df, hue="Species")
    plt.savefig("plots/pairplot.png")
    plt.close()

    # Correlation heatmap
    corr = df.iloc[:, :-1].corr()
    plt.figure(figsize=(6, 5))
    sns.heatmap(corr, annot=True, cmap="coolwarm")
    plt.title("Correlation Heatmap")
    plt.savefig("plots/correlation_heatmap.png")
    plt.close()

    print("Saved scatter plots, pairplot, and heatmap in /plots/")
    return df


if __name__ == "__main__":
    main()
