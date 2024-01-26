from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator


default_args = {
    "owner": "airflow",
    "retries": 5,
    "retry_delay": timedelta(minutes=1),
}

def get_sklearn():
    import sklearn
    print(f"scikit-learn version: {sklearn.__version__}")

with DAG(
    dag_id="dag_with_python_dependencies_v02",
    default_args=default_args,
    description="DAG with Python Dependencies",
    schedule_interval="@daily",
    start_date=datetime(2024, 1, 18, 3),
    catchup=False,
) as dag:
    get_sklearn = PythonOperator(
        task_id="get_sklearn", 
        python_callable=get_sklearn
    )
    
    get_sklearn