#!/bin/bash

# Set container and image names
CONTAINER_NAME=customer_container
RESULTS_DIR=./results

echo "Copying results from container to host..."
mkdir -p $RESULTS_DIR

# Copy all output files from the container to the host results folder
docker cp $CONTAINER_NAME:/app/pipeline/data_raw.csv $RESULTS_DIR/ 2>/dev/null
docker cp $CONTAINER_NAME:/app/pipeline/data_preprocessed.csv $RESULTS_DIR/ 2>/dev/null
docker cp $CONTAINER_NAME:/app/pipeline/insight1.txt $RESULTS_DIR/ 2>/dev/null
docker cp $CONTAINER_NAME:/app/pipeline/insight2.txt $RESULTS_DIR/ 2>/dev/null
docker cp $CONTAINER_NAME:/app/pipeline/insight3.txt $RESULTS_DIR/ 2>/dev/null
docker cp $CONTAINER_NAME:/app/pipeline/summary_plot.png $RESULTS_DIR/ 2>/dev/null
docker cp $CONTAINER_NAME:/app/pipeline/clusters.txt $RESULTS_DIR/ 2>/dev/null

echo "Stopping and removing container..."
docker stop $CONTAINER_NAME
docker rm $CONTAINER_NAME

echo "All results copied to 'results/' and container removed successfully!"