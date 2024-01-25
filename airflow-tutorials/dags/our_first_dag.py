from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    "owner": "airflow",
    "retries": 5,
    "retry_delay": timedelta(minutes=1),
}

with DAG(
    dag_id="our_first_dag_v5",
    default_args=default_args,
    description="Our first DAG",
    schedule_interval="@daily",
    start_date=datetime(2024, 1, 18, 3),
    catchup=False,
) as dag:
    # Tasks will be added here
    task1 = BashOperator(
        task_id="first_task", 
        bash_command="echo hello world, this is our first task")
    
    task2 = BashOperator(
        task_id="second_task", 
        bash_command="echo hello world, this is our second task")
    
    task3 = BashOperator(
        task_id="third_task", 
        bash_command="echo hello world, this is our third task")
    
    # task1.set_downstream(task2)
    # task1.set_downstream(task3)
    # task1 >> task2 >> task3
    task1 >> [task2, task3]