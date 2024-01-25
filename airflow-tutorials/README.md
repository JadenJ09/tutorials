### Installing airflow
pip install 'apache-airflow==2.8.0' \
 --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.8.0/constraints-3.8.txt"

### Indicating airflow working directories to current directories
export AIRFLOW_HOME=.

### Initializing airflow DB
airflow db init

### Checking ports usage
lsof -i or netstat -tuln
lsof - i :8080

### Running airflow webserver
airflow webserver -p 8080

### When running webserver indicates a SQLite database configuration error
"airflow.exceptions.AirflowConfigException: Cannot use relative path: `sqlite:///./airflow.db` to connect to sqlite. Please use absolute path such as `sqlite:////tmp/airflow.db`."

airflow config list

"Go to 'airflow.cfg'"
"Set an absolute path"
sql_alchemy_conn = sqlite:///'path/to/airflow.db'

"Restart airflow"
airflow webserver -p 8080 -D
airflow scheduler -D


### Fetching Docker Compose File
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.8.1/docker-compose.yaml'