# visualize.py
import sys
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import subprocess

def main():
    if len(sys.argv) < 2:
        print("Usage: python visualize.py <input_csv>")
        sys.exit(1)

    input_path = sys.argv[1]
    df = pd.read_csv("data_preprocessed.csv")

    # Example visualization: correlation heatmap
    plt.figure(figsize=(8,6))
    sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="Blues")
    plt.title("Correlation Heatmap")
    plt.tight_layout()
    plt.savefig("summary_plot.png")
    plt.close()

    print("Visualization complete. Plot saved as summary_plot.png")

    # Call next script
    subprocess.run(["python", "cluster.py", "data_preprocessed.csv"])

if __name__ == "__main__":
    main()
