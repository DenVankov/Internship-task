import time
import random

import requests

url = 'http://0.0.0.0:9980/upload/metrics/'

while True:
    for name in range(1, 11):
        value = round(random.uniform(10.5, 100.5), 4)
        data = {"metric_value": value, "metric_name": f'metric_{name}'}
        resp = requests.post(url, json=data)
        # print(data)
        # print(resp)
    time.sleep(5)
