# spotify-API
이 공간은 spotify API를 통해 PySpark를 연습하는 공간입니다 :)

# 준비물!
우리는 로컬 환경에서 실습을 진행하기 때문에, 아래와 같은 준비물들이 환경에 구성되어 있어야 해요.

### 설치 프로그램
1. Spark/spark-3.2.4-bin-hadoop3.2
2. Zeppelin/zeppelin-0.10.1-bin-all
a. Airflow/airflow-2.6.1

### 시작 명령어
#### Spark 시작 명령어 (job-submit을 할 예정이라면 필요 없음!)
``` bash
# sbin 디렉토리로 이동
$ ./start-master.sh

# localhost 에서 spark host 확인하기!
$ ./start-worker.sh spark://neivekim76.local:7077 -m 1g
```

#### Zeppelin 시작 명령어
``` bash
# bin 디렉토리로 이동
$ ./zeppelin-daemon.sh
```

#### Airflow 시작 명령어
``` bash
$ airflow standalone
```
