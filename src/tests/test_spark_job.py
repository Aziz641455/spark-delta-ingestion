import pytest
from pyspark.sql import SparkSession
from src.spark_job import add_columns

@pytest.fixture(scope="module")
def spark():
    return SparkSession.builder.master("local").appName("Test Suite").getOrCreate()

def test_add_columns(spark):
    df = spark.createDataFrame([(1, "test")], ["id", "value"])
    df = add_columns(df)

    assert "ingestion_tms" in df.columns
    assert "batch_id" in df.columns
