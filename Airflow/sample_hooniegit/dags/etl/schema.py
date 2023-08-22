# IMPORT MODULES
import pendulum, os
from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash import BashOperator
from airflow.models.variable import Variable

# >> CHANGE THIS DIRECTORY TO RUN THIS SCRIPT
os.chdir('/Users/kimdohoon/git/Spotify-Playground/spotify-API')
now_dir = os.getcwd()

# SET TIMEZONE
local_tz = pendulum.timezone('Europe/London')

# DAG SETTINGS
default_args = {
    'owner': 'pd24',
    'depends_on_past': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}
dag = DAG(
    dag_id = 'team_info_demo_4',
    description = 'pipeline loading spotify datas using api requests',
    tags = ['spark', 'uri', 'word'],
    max_active_runs = 1,
    concurrency = 1,
    start_date=datetime(year=2023, month=6, day=20, hour=0, minute=0, tzinfo=local_tz),
    schedule_interval = '30 6 * * *',
    user_defined_macros={'local_dt': lambda execution_date: execution_date.in_timezone(local_tz).strftime("%Y-%m-%d %H:%M:%S")},
    default_args = default_args
)

# start.spark
# 쉘 스크립트(스파크 마스터와 워커의 실행 여부를 확인하고, 꺼져 있으면 실행)를 실행하는 오퍼레이터
run_spark = BashOperator(
    task_id='run.spark',
    bash_command=f'''
    if sh {now_dir}/Airflow/sample_hooniegit/sh/run-spark.sh $SPARK_HOME; then echo "Run Spark"
    else echo "Spark is already running."
    fi
    ''',
    dag=dag
)

# spark.task.1
# 쉘 스크립트(스파크 잡을 받아서 마스터에 전송)를 실행하는 오퍼레이터
spark_task_1 = BashOperator(
    task_id='spark.task.1',
    bash_command=f'''
    sh {now_dir}/Airflow/sample_hooniegit/sh/pyspark-submit.sh \
    /Users/kimdohoon/git/hooniegit/Spark-demo/src/teams.py
    ''',
    dag=dag
)


# OPERATOR PROCEDURE
# start >> check_execute >> check_nowdir >> check_wishlist >> make_JSON_playlist >> make_DONE
run_spark >> spark_task_1