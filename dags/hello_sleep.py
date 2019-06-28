from time import sleep
from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

def print_hello():
    return 'Hello!'

def sleep_two_seconds():
    sleep(2)
    return 'Good morning!'

dag = DAG('hello_sleep', description='Hello and sleep tasks',
        schedule_interval='* * * * *',
        start_date=datetime(2019, 6, 21), catchup=False)

hello_operator_1 = PythonOperator(task_id='hello_task_1', python_callable=print_hello, dag=dag)

hello_operator_2 = PythonOperator(task_id='hello_task_2', python_callable=print_hello, dag=dag)

sleep_operator = PythonOperator(task_id='sleep_task', python_callable=sleep_two_seconds, dag=dag)

hello_operator_1 >> sleep_operator >> hello_operator_2