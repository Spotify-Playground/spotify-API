#!/bin/bash

spark_dir=$1

# run master
# 각자의 spark 경로 내 start-master.sh로 새로 지정 필요!
$spark_dir/sbin/start-master.sh

# run worker
# 각자의 spark 경로 내 start-worker.sh로 새로 지정 필요!
$spark_dir/sbin/start-worker.sh \
spark://neivekim76.local:7077 \
-m 1g