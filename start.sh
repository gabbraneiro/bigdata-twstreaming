#!/bin/sh
./kafka/bin/zookeeper-server-stop.sh &
./kafka/bin/kafka-server-stop.sh &
./kafka/bin/zookeeper-server-start.sh ./kafka/config/zookeeper.properties &
./kafka/bin/kafka-server-start.sh ./kafka/config/server.properties

wait