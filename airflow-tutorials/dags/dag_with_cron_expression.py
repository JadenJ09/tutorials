from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    "owner": "airflow",
    "retries": 5,
    "retry_delay": timedelta(minutes=1),
}

with DAG(
    dag_id="dag_with_cron_expression_v04",
    default_args=default_args,
    description="Our first DAG with cron expression",
    schedule_interval= "0 3 * * Tue-Fri", #"@daily", # cron expression is used to schedule the DAG more precisely and detailed
    start_date=datetime(2024, 1, 18, 3),
    catchup=True,
) as dag:
    # Tasks will be added here
    task1 = BashOperator(
        task_id="first_task", 
        bash_command="echo Dag with cron expression")
    
    # task2 = BashOperator(
    #     task_id="second_task", 
    #     bash_command="echo hello world, this is our second task")
    
    # task3 = BashOperator(
    #     task_id="third_task", 
    #     bash_command="echo hello world, this is our third task")
    
    # task1.set_downstream(task2)
    # task1.set_downstream(task3)
    # task1 >> task2 >> task3
    # task1 >> [task2, task3]