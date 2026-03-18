import boto3
import os
from dotenv import load_dotenv

load_dotenv()

# AWS Configuration
AWS_REGION = os.getenv("AWS_REGION")   # Change to your region
S3_BUCKET_NAME =  os.getenv("S3_BUCKET_NAME")# Must be globally unique


REDSHIFT_DATABASE = os.getenv("REDSHIFT_DATABASE")
REDSHIFT_DB_USER = os.getenv("REDSHIFT_DB_USER")
REDSHIFT_WORKGROUP = os.getenv("REDSHIFT_WORKGROUP")
REDSHIFT_IAM_ROLE_ARN = os.getenv("REDSHIFT_IAM_ROLE_ARN")

_s3_client = None
_redshift_client = None

def get_s3_client():
    global _s3_client

    if _s3_client is None:
        _s3_client = boto3.client(
            "s3",
            region_name=AWS_REGION
        )

    return _s3_client

def get_redshift_client():
    global _redshift_client
    if _redshift_client is None:
        _redshift_client = boto3.client(
            "redshift-data",
            region_name=AWS_REGION
        )
    return _redshift_client
