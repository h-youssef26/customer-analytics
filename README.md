#  Customer Analytics — Big Data Assignment 1

##  Overview

This project demonstrates a **complete data analytics workflow** from **preprocessing** and **analysis** to **visualization** and **clustering** all running inside a **Docker container**.  

It uses the **Ames Housing dataset** to explore insights, visualize patterns, and apply K-Means clustering for data segmentation.

---

##  Docker Setup & Execution

###  Build the Docker Image
Run this command inside your project folder (where the `Dockerfile` is located):

```bash
docker build -t customer_analytics .

```

### Execute the Scripts

```bash

docker run -it --name customer_container customer_analytics /bin/bash

python preprocess.py
python analytics.py
python visualize.py
python cluster.py
```

## Copy Results and Stop Container

After execution, use the provided script to copy all outputs from the container to your local system and clean up:

```bash 
bash summary.sh
```
### Project Structure
```bash 
customer-analytics/
│
├── preprocess.py         # Data cleaning, encoding, scaling, PCA, and discretization
├── analytics.py          # Textual insights generation (3 insights saved as text files)
├── visualize.py          # Data visualization (histogram / heatmap saved as PNG)
├── cluster.py            # K-Means clustering and output summary
├── summary.sh            # Copies results from container and stops it
├── Dockerfile            # Defines environment, dependencies, and entrypoint
├── requirements.txt      # List of Python dependencies
├── README.md             # Documentation (this file)
└── data/
    └── AmesHousing.csv   # Original dataset
```

### Detailed Execution Flow
## preprocess.py

Loads AmesHousing.csv.

Performs:

1- Data Cleaning: Removes nulls and duplicates.

2- Feature Transformation: Encodes categorical columns, scales numerical ones.

3- Dimensionality Reduction: Applies PCA to reduce dimensions.

4- Discretization: Bins one numeric column into ranges.

Saves the result as:

```bash
data_preprocessed.csv
```

### analytics.py

## Generates three textual insights about the dataset.

Each is saved separately:

```bash
insight1.txt
insight2.txt
insight3.txt
```

## Example Insights:

1- Average sale price per neighborhood

2- Correlation between overall quality and sale price

3- Top 5 most expensive house styles

## visualize.py

Creates one meaningful visualization, such as:

Histogram of sale prices

Correlation heatmap

Saves as:

```bash
summary_plot.png
```

## cluster.py

Applies K-Means clustering on selected numeric features.

Determines number of samples per cluster and saves to:

```bash
clusters.txt
```

Example Output:
Cluster 0: 425 samples
Cluster 1: 312 samples
Cluster 2: 189 samples

## summary.sh

This script automates post-processing tasks:

```bash
#!/bin/bash
# Create local results folder
mkdir -p /customer-analytics/results

# Copy all generated outputs from container to host
docker cp analytics_container:/customer-analytics/data_preprocessed.csv customer-analytics/results/
docker cp analytics_container:/customer-analytics/insight1.txt customer-analytics/results/
docker cp analytics_container:/customer-analytics/insight2.txt customer-analytics/results/
docker cp analytics_container:/customer-analytics/insight3.txt customer-analytics/results/
docker cp analytics_container:/customer-analytics/summary_plot.png customer-analytics/results/
docker cp analytics_container:/customer-analytics/clusters.txt customer-analytics/results/

```

### Dependencies

All dependencies are listed in requirements.txt.
Main ones include:

```bash
pandas
numpy
scikit-learn
matplotlib
seaborn
```

If running outside Docker, install them using:

```bash
pip install -r requirements.txt
```

### Example Screenshot

<img width="800" height="600" alt="summary_plot" src="https://github.com/user-attachments/assets/19658447-e0c5-451a-a658-63d82b9b0540" />

### Example Command Summary

```bash
docker build -t customer_analytics .
docker run -it --name analytics_container customer-analytics
python ingest.py AmesHousing.csv
python preprocess.py
python analytics.py
python visualize.py
python cluster.py
bash summary.sh
```

# Authors

## Hajar Muhammad Abdelhaliem - 221000755
## Heba Youssef - 231000723
## Omar Magdy - 231000967

### Nile University — CSCI461: Introduction to Big Data
### Fall 2025
