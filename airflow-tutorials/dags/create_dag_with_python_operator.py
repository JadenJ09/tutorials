from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

default_args = {
    "owner": "airflow",
    "retries": 5,
    "retry_delay": timedelta(minutes=1),
}

# xcom is a way to share data between tasks but it is not recommended to use it for large data more than 48KB
def greet(ti):
    # name = ti.xcom_pull(task_ids="get_name")
    first_name = ti.xcom_pull(key="first_name", task_ids="get_name")
    last_name = ti.xcom_pull(key="last_name", task_ids="get_name")
    age = ti.xcom_pull(key="age", task_ids="get_age")
    print(f"Hello world! My name is {first_name} {last_name}, and I am {age} years old.")
    
    
def get_name(ti):
    ti.xcom_push(key="first_name", value="Jay")
    ti.xcom_push(key="last_name", value="Gatsby")
    
def get_age(ti):
    ti.xcom_push(key="age", value=26)    


with DAG(
    dag_id="create_dag_with_python_operator_v06",
    default_args=default_args,
    description="Create DAG with PythonOperator",
    schedule_interval="@daily",
    start_date=datetime(2024, 1, 18, 3),
    catchup=False,
) as dag:
    # Tasks will be added here
    task1 = PythonOperator(
        task_id="greet", 
        python_callable=greet,
        # op_kwargs={"age": 26}
    )
    
    task2 = PythonOperator(
        task_id="get_name", 
        python_callable=get_name
    )
    
    task3 = PythonOperator(
        task_id="get_age", 
        python_callable=get_age
    )
    
    [task2, task3] >> task1
    # task1
    # task1.set_downstream(task2)
    # task1.set_downstream(task3)
    # task1 >> task2 >> task3
    # task1 >> [task2, task3]