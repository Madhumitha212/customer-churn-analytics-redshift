# Customer Churn Analytics Warehouse using Amazon Redshift Serverless

## Project Overview

This project demonstrates integration between **Python** and **AWS analytical services** to build an automated telecom customer churn analytics warehouse.

The pipeline performs:

* Uploading telecom datasets to Amazon S3
* Loading raw CSV files into Amazon Redshift Serverless
* Creating staging tables
* Building a final analytical warehouse table
* Running churn analysis queries
* Performing warehouse optimization using ANALYZE and VACUUM
* Automating all SQL execution through Python scripts

---

## Development Environment

| Component            | Details                    |
| -------------------- | -------------------------- |
| OS                   | Windows with WSL (Ubuntu)  |
| Cloud Environment    | AWS                        |
| Programming Language | Python 3.x                 |
| AWS SDK              | Boto3                      |
| Data Warehouse       | Amazon Redshift Serverless |
| Storage              | Amazon S3                  |

All commands were executed inside the **WSL terminal**.

---

## AWS Services Used

### Amazon S3

Used for storing raw telecom CSV datasets before loading into Redshift.

### Amazon Redshift Serverless

Used to:

* Create staging tables
* Load raw data using COPY command
* Create analytical warehouse table
* Execute SQL analysis queries

### IAM (Identity and Access Management)

Used to securely configure AWS permissions.

IAM role attached to Redshift Serverless allows access to S3 bucket.

### Python + Boto3

Used to automate Redshift SQL execution through Python scripts.

---

## AWS CLI Configuration

Before running the project, configure AWS credentials.

Run:

```bash
aws configure
```

Enter:

```text
AWS Access Key ID: <your-access-key>
AWS Secret Access Key: <your-secret-key>
Default region name: <your-region>
Default output format: json
```

Example:

```text
AWS Access Key ID: AKIA*************
AWS Secret Access Key: *********************
Default region name: us-east-1
Default output format: json
```

Credentials are stored in:

```text
~/.aws/credentials
```

### Test Configuration

Run:

```bash
aws s3 ls
```

If successful, it displays available S3 buckets.

---

## Dataset

Source: 
Kaggle Telecom Customer Churn Dataset
https://www.kaggle.com/datasets/shilongzhuang/telecom-customer-churn-by-maven-analytics 

Files used:

* telecom_customer_churn.csv
* zip_code_population.csv

---

## Project Structure

```text
customer_churn_redshift/
├── config/
│   └── get_client.py
│
├── scripts/
│   ├── upload_to_s3.py
|   ├── run_queries.py
│   ├── table_creation.py
│   ├── load_data.py
│   ├── create_final_table.py
│   └── analysis.py
│
├── document
│   ├── s3_bucket_creation.txt
│   └── serverless_cluster_creation.txt
│
├── screenshots/
│
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Environment Variables

Create `.env` file:

```env
AWS_REGION=your-region
REDSHIFT_DATABASE=telecom_dw
REDSHIFT_WORKGROUP=your-workgroup-name
REDSHIFT_IAM_ROLE_ARN=your-iam-role-arn
S3_BUCKET_NAME=your-bucket-name
```

---

## requirements.txt

```txt
boto3
python-dotenv
```

---

## S3 Bucket Structure

Upload files into Amazon S3:

```text
telecom-redshift-assignment/
└── raw/
    ├── telecom_customer_churn.csv
    └── zip_code_population.csv
```

---

## Redshift Serverless Configuration

| Parameter | Value             |
| --------- | ----------------- |
| Namespace | telecom-namespace |
| Workgroup | telecom-workgroup |
| Database  | telecom_dw        |

IAM role attached with Amazon S3 read permission.

---

## Running the Project (WSL)

### 1. Open WSL

### 2. Install dependencies

```bash
sudo apt update
sudo apt install python3 python3-pip
pip3 install -r requirements.txt
```

### 3. Clone repository

```bash
git clone <https://github.com/Madhumitha212/customer-churn-analytics-redshift>
cd customer_churn_redshift
```

### 4. Create virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 5. Configure AWS CLI

```bash
aws configure
```

### 6. Run scripts in sequence

```bash
python3 -m scripts.upload_to_s3
python3 -m scripts.table_creation
python3 -m scripts.load_data
python3 -m scripts.create_final_table
python3 -m scripts.analysis
```

---

## Data Warehouse Workflow

### Step 1 — Create Staging Tables

Creates:

* staging_customer_churn
* staging_zip_population

---

### Step 2 — Load Data from S3

Uses Redshift COPY command with:

* CSV format
* IGNOREHEADER 1
* DELIMITER ','

---

### Step 3 — Create Final Analytical Table

Creates:

final_customer_churn_analysis

Columns included:

* customer_id
* city
* zip_code
* population
* tenure
* monthly_charges
* total_charges
* customer_status

---

### Step 4 — Run Analytical Queries

Generates:

1. Churn rate across all customers
2. Top cities with highest churn
3. Customer churn distribution by tenure group
4. Total revenue lost due to churn
5. Population vs customer count by zip code

---

### Step 5 — Warehouse Maintenance

Runs:

* ANALYZE
* VACUUM

---

## SQL Optimization Used

### DISTKEY

zip_code chosen to improve join efficiency.

### SORTKEY

customer_id chosen for sorting and filtering performance.

---

## Redshift Concepts Used

### Redshift Architecture

Amazon Redshift Serverless consists of:

* Namespace = metadata and storage
* Workgroup = compute resources

### Columnar Storage

Redshift stores data by columns, improving analytical performance.

---

## Screenshots Included

screenshots folder contains:

* S3 bucket structure
* Redshift namespace
* Redshift workgroup

---

## Assumptions

* AWS account available
* IAM role configured correctly
* AWS CLI configured
* CSV files uploaded to S3
* Python dependencies installed

---

## Cleanup

After completion:

* Pause or delete Redshift workgroup
* Keep S3 storage minimal

---

## Author

**R Madhumitha**
