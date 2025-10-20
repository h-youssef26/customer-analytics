# Use base image
FROM python:3.11-slim

# Install dependencies
RUN pip install pandas numpy matplotlib seaborn scikit-learn scipy requests

# Create working directory
WORKDIR /app/pipeline/

# Copy all project files
COPY . /app/pipeline/

# Set default command when container runs
CMD ["/bin/bash"]
