from config.get_client import *
from botocore.exceptions import *

def upload_file_to_s3(local_file, bucket, s3_key):
    """Upload a file to S3."""
    s3 = get_s3_client()
    try:
        s3.upload_file(local_file, bucket, s3_key)
        print(f"Uploaded {local_file} to s3://{bucket}/{s3_key}")

    except FileNotFoundError:
        print("Local file not found.")

    except NoCredentialsError:
        print("AWS credentials not available.")

    except ClientError as e:
        print(f"Upload failed: {e}")

if __name__ == "__main__":
    upload_file_to_s3("dataset/telecom_customer_churn.csv", S3_BUCKET_NAME, "raw/telecom_customer_churn.csv")
    upload_file_to_s3("dataset/telecom_zipcode_population.csv", S3_BUCKET_NAME, "raw/telecom_zipcode_population.csv")