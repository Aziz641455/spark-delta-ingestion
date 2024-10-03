import sys
import uuid
from datetime import datetime
from pyspark.sql import SparkSession
from pyspark.sql.functions import lit

def add_columns(df):
    ingestion_tms = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    batch_id = str(uuid.uuid4())

    df = df.withColumn("ingestion_tms", lit(ingestion_tms))
    df = df.withColumn("batch_id", lit(batch_id))
    
    return df

def ingest_csv_to_delta(input_path, output_path, header_option):
    spark = SparkSession.builder \
        .appName("CSV to Delta Ingestion Job") \
        .getOrCreate()

    # Read CSV file(s)
    df = spark.read.option("header", header_option).csv(input_path)
    
    # Add columns
    df = add_columns(df)
    
    # Write to Delta in append mode
    df.write.format("delta").mode("append").save(output_path)

    spark.stop()

if __name__ == "__main__":
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    header_option = sys.argv[3]
    
    ingest_csv_to_delta(input_path, output_path, header_option)
