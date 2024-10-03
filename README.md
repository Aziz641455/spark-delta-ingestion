# Spark DeltaLake Ingestion

This project provides a solution for ingesting CSV files into DeltaLake using PySpark. It adds additional columns for ingestion timestamp and batch ID, and uses append mode to save data atomically.

## Setup

1. Clone the repository:
    ```bash
    git clone <repository-url>
    ```

2. Build and run the Docker containers:
    ```bash
    docker-compose up --build
    ```

## Running the Job

The Spark job can be executed by running:
```bash
docker exec -it spark-job \
  /opt/spark/bin/spark-submit \
  /opt/spark/jobs/spark_job.py \
  /data/input/ /data/output/ true
