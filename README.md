# 👪 spotify-API
이 공간은 spotify API를 통해 PySpark를 연습하는 공간입니다 :)

# 📚 준비물!
우리는 로컬 환경에서 실습을 진행하기 때문에, 아래와 같은 준비물들이 환경에 구성되어 있어야 해요.

### 🧰 설치 프로그램
1. Spark/spark-3.2.4-bin-hadoop3.2
2. Zeppelin/zeppelin-0.10.1-bin-all
3. Airflow/airflow-2.6.1 (DAG 연습을 하고 싶은 경우에만!)

### 🏃 시작 명령어
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

# 🧐 어디에서 무슨 공부를 하면 되나요?
### 1. 🖥️ issue
'issue' 부분은 각자가 공부한 내용, 또는 공유하고자 하는 자료 등을 자유롭게 적는 도화지입니다!
다른 사람들이 올린 자료들도 적절히 참고하면서 사용해주시면 좋을 것 같아요.

### 2. 📂 directory
정리중!
