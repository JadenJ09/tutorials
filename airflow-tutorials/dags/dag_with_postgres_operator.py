from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator

default_args = {
    "owner": "airflow",
    "retries": 5,
    "retry_delay": timedelta(minutes=1),
}

with DAG(
    dag_id="dag_with_postgres_operator_v03",
    default_args=default_args,
    description="DAG with Postgres Operator",
    schedule_interval="0 0 * * *",
    start_date=datetime(2024, 1, 18, 3),
    catchup=True,
) as dag:
    create_table = PostgresOperator(
        task_id="create_postgres_table",
        postgres_conn_id="postgres_localhost",
        sql="""
            CREATE TABLE IF NOT EXISTS DAG_RUNS (
                dt date,
                dag_id character varying(50),
                primary key (dt, dag_id)
            );
        """
    )
    
    insert_table = PostgresOperator(
        task_id="insert_postgres_table",
        postgres_conn_id="postgres_localhost",
        sql="""
            INSERT INTO DAG_RUNS (dt, dag_id) VALUES
            ('{{ ds }}', '{{ dag.dag_id }}');
        """
    )
    
    delete_data = PostgresOperator(
        task_id="delete_data",
        postgres_conn_id="postgres_localhost",
        sql="""
            DELETE FROM DAG_RUNS WHERE 
            dt = '{{ ds }}' and dag_id = '{{ dag.dag_id }}';
        """
    )
    
    create_table >> delete_data >> insert_table
    
    # insert_data = PostgresOperator(
    #     task_id="insert_data",
    #     postgres_conn_id="postgres_default",
    #     sql="""
    #         INSERT INTO users VALUES
    #         ('