import sys
import pandas as pd

def main():
    if len(sys.argv) < 2:
        print("Usage: python ingest.py <dataset_path>")
        sys.exit(1)

    dataset_path = sys.argv[1]

    df = pd.read_csv(dataset_path)
    df.to_csv("data_raw.csv", index=False)

    print("Data ingested and saved as data_raw.csv")

if __name__ == "__main__":
    main()
