from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator

default_args = {
    "owner": "airflow",
    "retries": 5,
    "retry_delay": timedelta(minutes=1),
}

with DAG(
    dag_id="dag_with_catchup_and_backfill_v02",
    default_args=default_args,
    description="DAG with Catchup and Backfill",
    schedule_interval="@daily",
    start_date=datetime(2024, 1, 18, 3),
    catchup=False,
) as dag:
    task1 = BashOperator(
        task_id="task1", 
        bash_command="echo hello world, this is our first task")
    
    