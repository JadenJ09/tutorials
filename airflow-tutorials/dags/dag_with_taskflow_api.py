from airflow.decorators import dag, task
from datetime import datetime, timedelta

default_args = {
    "owner": "airflow",
    "retries": 5,
    "retry_delay": timedelta(minutes=1),
}

@dag(
    dag_id="dag_with_taskflow_api_v02",
    default_args=default_args,
    description="DAG with Taskflow API",
    schedule_interval="@daily",
    start_date=datetime(2024, 1, 18, 3),
    catchup=False,
)
def hello_world_etl():
    @task(multiple_outputs=True)
    def get_name():
        # return "Jay Gatsby"
        return {
            "first_name": "Jay",
            "last_name": "Gatsby"
        }
    
    @task
    def get_age():
        return 26
    
    @task
    def greet(first_name: str, last_name: str, age: int):
        print(f"Hello world! My name is {first_name} {last_name}, and I am {age} years old.")
        
    # name = get_name()
    name_dict = get_name()
    age = get_age()
    greet(first_name=name_dict["first_name"], last_name=name_dict["last_name"], age=age)
    
greet_dag = hello_world_etl()