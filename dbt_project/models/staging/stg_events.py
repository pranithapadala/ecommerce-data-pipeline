import boto3
import pandas as pd
import io

# This function is the core of a Python dbt model
def model(dbt, duckdb):
    
    # This tells dbt that this model is a table, not a view
    dbt.config(materialized="table")

    # --- Configuration ---
    s3_bucket_name = "pranitha-ecom-data"
    s3_object_key = "raw-data/events.csv"
    # ---------------------

    print(f"--> Starting: Reading {s3_object_key} from bucket {s3_bucket_name}")

    # Use boto3 to get the object from S3 (this is what worked in your script)
    s3 = boto3.client('s3')
    response = s3.get_object(Bucket=s3_bucket_name, Key=s3_object_key)
    
    # The data is in the 'Body' of the response. We read it into memory.
    csv_content = response['Body'].read()

    # Use pandas to read the in-memory CSV data
    # We need to specify data types to avoid errors
    df = pd.read_csv(
        io.BytesIO(csv_content),
        dtype={
            'timestamp': 'float64',
            'visitorid': 'str',
            'event': 'str',
            'itemid': 'str',
            'transactionid': 'str'
        }
    )
    
    print(f"--> Success: Read {len(df)} rows from S3.")
    return df