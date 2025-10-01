import pandas as pd

# === Problem 2: Combining Data ===
# Goal: Merge the features (X) and labels (y) into one DataFrame df.

def main():
    # Load features and labels from Problem 1 outputs
    X = pd.read_csv("data/iris_features.csv")
    y = pd.read_csv("data/iris_labels.csv")

    # Combine them side by side
    df = pd.concat([X, y], axis=1)

    # Print preview
    print("=== Combined DataFrame (df) preview ===")
    print(df.head(), "\n")

    # Check shape for sanity: should be (150, 5)
    print(f"DataFrame shape: {df.shape}\n")

    # Save combined DataFrame for later use
    df.to_csv("data/iris_combined.csv", index=False)
    print("Data saved: 'data/iris_combined.csv'")

if __name__ == "__main__":
    main()
