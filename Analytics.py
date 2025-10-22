# analytics.py
import pandas as pd

# Load preprocessed data
df = pd.read_csv("data_preprocessed.csv")

# 1. Insight 1: Correlation with SalePrice
if 'SalePrice' in df.columns:
    corr = df.corr(numeric_only=True)['SalePrice'].sort_values(ascending=False)
    top_corr = corr[1:6]  # top 5 correlated features (excluding itself)
    insight1 = "Top 5 features most correlated with SalePrice:\n"
    insight1 += top_corr.to_string()
else:
    insight1 = "SalePrice column not found in dataset."

with open("insight1.txt", "w") as f:
    f.write(insight1)


# 2. Insight 2: Most common category for a categorical feature

cat_cols = df.select_dtypes(include="object").columns
if len(cat_cols) > 0:
    col = cat_cols[0]
    most_common = df[col].mode()[0]
    freq = df[col].value_counts().iloc[0]
    insight2 = f"Most common category in '{col}' is '{most_common}' appearing {freq} times."
else:
    insight2 = "No categorical columns found in dataset."

with open("insight2.txt", "w") as f:
    f.write(insight2)



# 3. Insight 3: Numeric statistics summary
num_cols = df.select_dtypes(include=["int64", "float64"]).columns
desc = df[num_cols].describe().T[['mean', 'std', 'min', 'max']]
insight3 = "Summary statistics for numeric columns:\n" + desc.to_string()

with open("insight3.txt", "w") as f:
    f.write(insight3)

print("Insights generated: insight1.txt, insight2.txt, insight3.txt")
