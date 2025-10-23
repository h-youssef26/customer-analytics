import pandas as pd
import subprocess
import sys
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.decomposition import PCA

def main():
    if len(sys.argv) < 2:
        print("Usage: python preprocess.py <input_csv>")
        sys.exit(1)

    input_path = sys.argv[1]
    df = pd.read_csv("data_raw.csv")

    # ---- Data Cleaning ----
    df = df.drop_duplicates()
    df = df.fillna(df.mean(numeric_only=True))

    # ---- Feature Transformation ----
    for col in df.select_dtypes(include="object"):
        df[col] = LabelEncoder().fit_transform(df[col].astype(str))

    num_cols = df.select_dtypes(include=["int64", "float64"]).columns
    df[num_cols] = StandardScaler().fit_transform(df[num_cols])

    # ---- Dimensionality Reduction ----
    df_reduced = df.iloc[:, :5]

    # ---- Discretization ----
    if df_reduced.shape[1] > 0:
        df_reduced["binned_feature"] = pd.cut(df_reduced.iloc[:, 0], bins=3, labels=["Low", "Medium", "High"])

    df_reduced.to_csv("data_preprocessed.csv", index=False)
    print("Preprocessing complete. Data saved as data_preprocessed.csv")

    # ---- Call next script ----
    subprocess.run(["python", "analytics.py", "data_preprocessed.csv"], check=True)

if __name__ == "__main__":
    main()
