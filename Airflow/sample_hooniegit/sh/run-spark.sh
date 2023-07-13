#!/bin/bash

# run master
# 각자의 spark 경로 내 start-master.sh로 새로 지정 필요!
/Users/kimdohoon/app/spark/spark-3.2.4-bin-hadoop3.2/sbin/start-master.sh

# run worker
# 각자의 spark 경로 내 start-worker.sh로 새로 지정 필요!
/Users/kimdohoon/app/spark/spark-3.2.4-bin-hadoop3.2/sbin/start-worker.sh \
spark://neivekim76.local:7077 \
-m 1g각