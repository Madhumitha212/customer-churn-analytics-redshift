from config.get_client import *
import time

def run_redshift_query(sql):
    redshift_client = get_redshift_client()
    response = redshift_client.execute_statement(
        Database=REDSHIFT_DATABASE,
        Sql=sql,
        WorkgroupName=REDSHIFT_WORKGROUP
    )
    statement_id = response['Id']
    # Wait until query finishes
    while True:
        status = redshift_client.describe_statement(Id=statement_id)
        if status['Status'] in ['FINISHED', 'FAILED', 'ABORTED']:
            break
        time.sleep(2)
    if status['Status'] == 'FAILED':
        raise Exception(f"Query failed: {status['Error']}")
    return redshift_client.get_statement_result(Id=statement_id) if "SELECT" in sql.upper() else None