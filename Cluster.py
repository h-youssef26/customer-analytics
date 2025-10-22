# cluster.py
import pandas as pd
from sklearn.cluster import KMeans

# Load the preprocessed dataset
df = pd.read_csv("data_preprocessed.csv")


# 1. Select subset of features
# Use only numeric columns for clustering
num_cols = df.select_dtypes(include=["int64", "float64"]).columns

# Use first few numeric columns to simplify clustering
subset = df[num_cols].iloc[:, :5]  # first 5 numeric columns


# 2. Apply K-Means Clustering
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
df['Cluster'] = kmeans.fit_predict(subset)

# 3. Count samples per cluster
cluster_counts = df['Cluster'].value_counts().sort_index()

# Prepare output text
output = "Number of samples per cluster:\n"
for cluster_id, count in cluster_counts.items():
    output += f"Cluster {cluster_id}: {count} samples\n"

# Save to clusters.txt
with open("clusters.txt", "w") as f:
    f.write(output)

print("Clustering complete. Results saved in clusters.txt")
