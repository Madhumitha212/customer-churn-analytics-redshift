from config.get_client import *
from scripts.run_queries import *

def load_data():
    load_churn = f"""
        COPY raw_customer_churn
        FROM 's3://{S3_BUCKET_NAME}/raw/telecom_customer_churn.csv'
        IAM_ROLE '{REDSHIFT_IAM_ROLE_ARN}'
        FORMAT AS CSV
        IGNOREHEADER 1;
    """

    load_zip_population = f"""
        COPY staging_zip_population
        FROM 's3://{S3_BUCKET_NAME}/raw/telecom_zipcode_population.csv'
        IAM_ROLE '{REDSHIFT_IAM_ROLE_ARN}'
        FORMAT AS CSV
        IGNOREHEADER 1;
    """

    run_redshift_query(load_churn)
    run_redshift_query(load_zip_population)

if __name__ == "__main__":
    load_data()
