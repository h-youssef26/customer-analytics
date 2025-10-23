# cluster.py
import sys
import pandas as pd
from sklearn.cluster import KMeans

def main():
    if len(sys.argv) < 2:
        print("Usage: python cluster.py <input_csv>")
        sys.exit(1)

    input_path = sys.argv[1]
    df = pd.read_csv("data_preprocessed.csv")

    # Select only numeric columns
    num_cols = df.select_dtypes(include=["float64", "int64"]).columns
    subset = df[num_cols].iloc[:, :5]

    kmeans = KMeans(n_clusters=3, random_state=42)
    df["cluster"] = kmeans.fit_predict(subset)

    cluster_counts = df["cluster"].value_counts().sort_index()

    # Save cluster summary
    with open("clusters.txt", "w") as f:
        for cluster_id, count in cluster_counts.items():
            f.write(f"Cluster {cluster_id}: {count} samples\n")

    print("Clustering complete. Results saved as clusters.txt")

if __name__ == "__main__":
    main()
