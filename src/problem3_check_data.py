import pandas as pd

# === Problem 3: Checking the Data ===
# Goal: Inspect dataset quality and structure.

def main():
    # Load the combined dataset from Problem 2
    df = pd.read_csv("data/iris_combined.csv")

    # Open a report file to store inspection results
    with open("data/iris_data_report.txt", "w") as report:
        report.write("=== Iris Data Inspection Report ===\n\n")

        # 1. Look at a single row (4th sample, index 3)
        row = df.iloc[3]
        report.write("4th Sample (Index 3):\n")
        report.write(str(row) + "\n\n")
        print("4th sample:\n", row, "\n")

        # 2. Count how many samples exist for each label
        label_counts = df["Species"].value_counts()
        report.write("Label Counts (Species):\n")
        report.write(str(label_counts) + "\n\n")
        print("Label counts:\n", label_counts, "\n")

        # 3. Check for missing values
        missing = df.isnull().sum()
        report.write("Missing Values per Column:\n")
        report.write(str(missing) + "\n\n")
        print("Missing values:\n", missing, "\n")

        # 4. Show summary stats
        summary = df.describe()
        report.write("Summary Statistics:\n")
        report.write(str(summary) + "\n\n")
        print("Summary statistics:\n", summary, "\n")

    print("Inspection report saved: 'data/iris_data_report.txt'")

if __name__ == "__main__":
    main()
