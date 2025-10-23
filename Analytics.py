# analytics.py
import sys
import pandas as pd
import subprocess

def main():
    if len(sys.argv) < 2:
        print("Usage: python analytics.py <input_csv>")
        sys.exit(1)

    input_path = sys.argv[1]
    df = pd.read_csv("data_preprocessed.csv")

    insights = []

    # Example textual insights
    insights.append(f"Dataset contains {df.shape[0]} rows and {df.shape[1]} columns.")
    insights.append(f"Mean of first numeric column: {df.select_dtypes(include=['float64', 'int64']).iloc[:,0].mean():.2f}")
    insights.append(f"Number of missing values: {df.isnull().sum().sum()}")

    for i, text in enumerate(insights, start=1):
        with open(f"insight{i}.txt", "w") as f:
            f.write(text)

    print("Analytics complete. Insights saved as insight1.txt, insight2.txt, insight3.txt")

    # Call next script
    subprocess.run(["python", "visualize.py", "data_preprocessed.csv"])

if __name__ == "__main__":
    main()
