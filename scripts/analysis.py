from scripts.run_queries import run_redshift_query

def run_analysis():

    print("\n--- Churn Rate ---")
    sql_churn_rate = """
    SELECT COUNT(*) AS total_customers,
           SUM(CASE WHEN customer_status='Churned' THEN 1 ELSE 0 END) AS churned_customers,
           ROUND(100.0 * SUM(CASE WHEN customer_status='Churned' THEN 1 ELSE 0 END) / COUNT(*), 2) AS churn_rate
    FROM final_customer_churn_analysis;
    """
    result = run_redshift_query(sql_churn_rate)
    for row in result['Records']:
        print([list(col.values())[0] for col in row])


    print("\n--- Total Revenue Lost Due to Churn ---")
    sql_revenue_lost = """
    SELECT SUM(total_charges) AS revenue_lost
    FROM final_customer_churn_analysis
    WHERE customer_status='Churned';
    """
    result = run_redshift_query(sql_revenue_lost)
    for row in result['Records']:
        print([list(col.values())[0] for col in row])


    print("\n--- Population vs Customer Count by Zip ---")
    sql_population_customers = """
    SELECT zip_code, population, COUNT(customer_id) AS customer_count
    FROM final_customer_churn_analysis
    GROUP BY zip_code, population
    ORDER BY customer_count DESC
    LIMIT 10;
    """
    result = run_redshift_query(sql_population_customers)
    for row in result['Records']:
        print([list(col.values())[0] for col in row])


    print("\n--- Top Cities with Highest Churn ---")
    sql_top_cities = """
    SELECT city,
           COUNT(*) AS churned_customers
    FROM final_customer_churn_analysis
    WHERE customer_status = 'Churned'
    GROUP BY city
    ORDER BY churned_customers DESC
    LIMIT 10;
    """
    result = run_redshift_query(sql_top_cities)
    for row in result['Records']:
        print([list(col.values())[0] for col in row])


    print("\n--- Churn Distribution by Tenure Group ---")
    sql_tenure_group = """
    SELECT
        CASE
            WHEN tenure BETWEEN 0 AND 12 THEN '0-12 Months'
            WHEN tenure BETWEEN 13 AND 24 THEN '13-24 Months'
            WHEN tenure BETWEEN 25 AND 48 THEN '25-48 Months'
            ELSE '49+ Months'
        END AS tenure_group,
        COUNT(*) AS churn_count
    FROM final_customer_churn_analysis
    WHERE customer_status = 'Churned'
    GROUP BY tenure_group
    ORDER BY tenure_group;
    """
    result = run_redshift_query(sql_tenure_group)
    for row in result['Records']:
        print([list(col.values())[0] for col in row])


if __name__ == "__main__":
    run_analysis()