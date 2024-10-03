FROM bitnami/spark:3.3.1

# Copy the spark job and scripts
COPY src /opt/spark/jobs/

# Install necessary Python dependencies including pytest
COPY requirements.txt .
RUN pip install -r requirements.txt

# Install pytest for testing
RUN pip install pytest

# Set the entry point for the job (optional: override with docker-compose command)
ENTRYPOINT ["spark-submit", "/opt/spark/jobs/spark_job.py"]
