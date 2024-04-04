from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'meoflaxz',
    'start_date': datetime(2021, 1, 1),
    'catchup': False
}

dag = DAG(
    dag_id: 'hello_world',
    default_args = default_args,
    schedule=timedelta(days=1)
)

tq = BashOperator(
    task_id = 'hello_world',
    bash_command = 'echo "Hello Guys"',
    dag = dag 
)

t1 >> t2