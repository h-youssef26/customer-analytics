# preprocess.py
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.preprocessing import KBinsDiscretizer

# Load data
df = pd.read_csv("AmesHousing.csv")

# =============================
# 1. Data Cleaning
# =============================
# Remove duplicates
df = df.drop_duplicates()

# Fill missing values
for col in df.columns:
    if df[col].dtype == "object":
        df[col] = df[col].fillna(df[col].mode()[0])
    else:
        df[col] = df[col].fillna(df[col].median())

# =============================
# 2. Feature Transformation
# =============================
# Identify numeric and categorical columns
num_cols = df.select_dtypes(include=["int64", "float64"]).columns
cat_cols = df.select_dtypes(include="object").columns

# Scale numeric columns
scaler = StandardScaler()
df_scaled = df.copy()
df_scaled[num_cols] = scaler.fit_transform(df[num_cols])

# =============================
# 3. Dimensionality Reduction
# =============================
# Apply PCA only on scaled numeric columns
pca = PCA(n_components=5)
pca_features = pca.fit_transform(df_scaled[num_cols])
pca_df = pd.DataFrame(pca_features, columns=[f"PCA_{i+1}" for i in range(5)])

# Add PCA features without removing categorical columns
df = pd.concat([df.reset_index(drop=True), pca_df], axis=1)

# =============================
# 4. Discretization
# =============================
# Discretize one numeric column (example: 'SalePrice' if exists)
if 'SalePrice' in df.columns:
    kb = KBinsDiscretizer(n_bins=4, encode='ordinal', strategy='quantile')
    df['SalePrice_binned'] = kb.fit_transform(df[['SalePrice']])

# =============================
# 5. Save processed data
# =============================
df.to_csv("data_preprocessed.csv", index=False)
print("Data preprocessing complete. Saved as data_preprocessed.csv (categorical columns preserved)")
