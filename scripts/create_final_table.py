from scripts.run_queries import run_redshift_query

def create_final_table():

    create_sql = f"""
    CREATE TABLE IF NOT EXISTS final_customer_churn_analysis (
        customer_id VARCHAR(50),
        city VARCHAR(100),
        zip_code VARCHAR(10),
        population INT,
        tenure INT,
        monthly_charges DECIMAL(10,2),
        total_charges DECIMAL(10,2),
        customer_status VARCHAR(50)
    )
    DISTKEY(zip_code)
    SORTKEY(customer_id);
    """

    insert_sql = f"""
    INSERT INTO final_customer_churn_analysis
    SELECT
        c.customer_id,
        c.city,
        c.zip_code,
        z.population,
        c.tenure,
        c.monthly_charges,
        c.total_charges,
        c.customer_status
    FROM raw_customer_churn c
    LEFT JOIN staging_zip_population z
    ON c.zip_code = z.zip_code;
    """

    print("Creating final table...")
    run_redshift_query(create_sql)

    print("Loading final analytical data...")
    run_redshift_query(insert_sql)

    print("Final table ready successfully.")

if __name__ == "__main__":
    create_final_table()