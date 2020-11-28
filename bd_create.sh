#!/bin/bash
set -e

clickhouse-client -n <<-EOSQL
    CREATE DATABASE click;
    CREATE TABLE click.clickhouse (metric_name String, metric_value Float64, time_stamp Float64) ENGINE = Log;
EOSQL