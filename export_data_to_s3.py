# export_to_s3.py
import duckdb
import boto3
from io import StringIO
import os

# --- Configuration ---
DB_FILE = "dbt_project/ecommerce.duckdb"
S3_BUCKET_NAME = "pranitha-ecom-data"
S3_FOLDER = "transformed-data"
TABLES_TO_EXPORT = ["transactions", "users", "products"]
# ---------------------

# Check if the database file exists
if not os.path.exists(DB_FILE):
    print(f"Error: Database file not found at '{DB_FILE}'")
    print("Please run 'dbt run' first to build the database.")
    exit()

print(f"Connecting to database: {DB_FILE}")
con = duckdb.connect(database=DB_FILE, read_only=True)

s3_client = boto3.client('s3')

for table_name in TABLES_TO_EXPORT:
    print(f"--> Exporting table: {table_name}")
    
    try:
        # Read the table from DuckDB into a Pandas DataFrame
        df = con.table(table_name).to_df()
        
        # Use an in-memory text buffer to write the CSV
        csv_buffer = StringIO()
        df.to_csv(csv_buffer, index=False)
        
        # Define the final path in S3
        s3_key = f"{S3_FOLDER}/{table_name}.csv"
        
        # Upload the in-memory CSV to S3
        s3_client.put_object(
            Bucket=S3_BUCKET_NAME,
            Key=s3_key,
            Body=csv_buffer.getvalue()
        )
        
        print(f"     Success! Uploaded to s3://{S3_BUCKET_NAME}/{s3_key}")
        
    except Exception as e:
        print(f"     FAILED to export table '{table_name}': {e}")

con.close()
print("\nExport process finished.")