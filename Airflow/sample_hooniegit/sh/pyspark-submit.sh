#!/bin/bash

SPARK_FILE="$1"

echo "$SPARK_FILE"

# 각자의 spark 경로 내 start-submit로 새로 지정 필요!
/Users/kimdohoon/app/spark/spark-3.2.4-bin-hadoop3.2/bin/spark-submit \
--master spark://neivekim76.local:7077 \
--executor-memory 512m \
--total-executor-cores 1 \
$SPARK_FILE
