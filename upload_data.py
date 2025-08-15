# upload_data.py
import boto3
import os

S3_BUCKET_NAME = "pranitha-ecom-data"
# 2. This is the name of your local data file.
LOCAL_FILE_PATH = "events.csv"
# 3. This is where the file will be stored in S3.
S3_OBJECT_NAME = "raw-data/events.csv"
# -----------------------------

# This script checks if your file exists before trying to upload.
if not os.path.exists(LOCAL_FILE_PATH):
    print(f"Error: The file '{LOCAL_FILE_PATH}' was not found.")
    print("Please make sure your data file is in the same folder as this script.")
else:
    print(f"Found file '{LOCAL_FILE_PATH}'. Starting upload...")
    
    # This creates a connection to AWS S3
    s3_client = boto3.client('s3')
    
    try:
        # This is the command that performs the upload
        s3_client.upload_file(LOCAL_FILE_PATH, S3_BUCKET_NAME, S3_OBJECT_NAME)
        print("✅ Success! Your file has been uploaded to S3.")
        print(f"   You can find it at: s3://{S3_BUCKET_NAME}/{S3_OBJECT_NAME}")
        
    except Exception as e:
        print(f"Error uploading file: {e}")