#!/bin/bash

SPARK_HOME=$1

# run master
$SPARK_HOME/sbin/start-master.sh

# run worker
$SPARK_HOME/sbin/start-worker.sh \
spark://neivekim76.local:7077 \
-m 3g