import pandas as pd
from sklearn.datasets import load_iris

# === Problem 1: Data Acquisition ===
# Goal: Load the iris dataset, separate features (X) and labels (y)

def main():
    # Load iris dataset from sklearn
    iris = load_iris()

    # Feature names provided by sklearn
    feature_names = iris.feature_names
    # Convert to more Pythonic column names (remove spaces, replace with underscores)
    feature_names = [name.replace(" (cm)", "").replace(" ", "_") for name in feature_names]

    # X = features DataFrame
    X = pd.DataFrame(data=iris.data, columns=feature_names)

    # y = labels (species) DataFrame
    y = pd.DataFrame(data=iris.target, columns=["Species"])

    # Print small previews to confirm
    print("=== Features (X) preview ===")
    print(X.head(), "\n")
    print("=== Target (y) preview ===")
    print(y.head(), "\n")

    # Save both to CSV files in the data/ folder for later use
    X.to_csv("data/iris_features.csv", index=False)
    y.to_csv("data/iris_labels.csv", index=False)

    print("Data saved: 'data/iris_features.csv' and 'data/iris_labels.csv'")

if __name__ == "__main__":
    main()
