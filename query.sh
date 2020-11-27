#!/bin/bash

curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"metric_value": 2.5, "metric_name": "awefw"}' \
  http://localhost:5000/upload/metrics/

curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"metric_value": 2.5, "metric_name": 2.5}' \
  http://localhost:5000/upload/metrics/
