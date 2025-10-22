# visualize.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load preprocessed data
df = pd.read_csv("data_preprocessed.csv")

# Select only numeric columns
num_cols = df.select_dtypes(include=["int64", "float64"]).columns
corr = df[num_cols].corr()

# Create a correlation heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(corr, cmap="coolwarm", annot=False)
plt.title("Correlation Heatmap of Numeric Features", fontsize=14)
plt.tight_layout()

# Save the plot
plt.savefig("summary_plot.png", dpi=300)
print("Visualization saved as summary_plot.png")
