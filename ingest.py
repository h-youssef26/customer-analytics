import sys
import pandas as pd
import subprocess

def main():
    if len(sys.argv) < 2:
        print("Usage: python ingest.py <dataset_path>")
        sys.exit(1)

    input_path = sys.argv[1]
    df = pd.read_csv("AmesHousing.csv")

    # Save raw copy
    df.to_csv("data_raw.csv", index=False)
    print("Ingestion complete. Data saved as data_raw.csv")

    # Call next script
    subprocess.run(["python", "preprocess.py", "data_raw.csv"])

if __name__ == "__main__":
    main()
