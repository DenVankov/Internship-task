from flask import Flask, make_response
from flask import request, jsonify
import json

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Start'


# {"metric_value": 2.5, "metric_name": "awefw"}
@app.route('/upload/metrics/', methods=['POST'])
def uploader():
    s = jsonify(request.json)
    dict_ = s.json
    keys = dict_.keys()
    if ("metric_name" not in keys) or ("metric_value" not in keys) or \
            (not isinstance(dict_['metric_name'], str)) or (not isinstance(dict_['metric_value'], float)):
        resp = make_response("Bad request\n", 400)
        return resp
    resp = make_response("OK\n", 200)
    return resp


if __name__ == '__main__':
    app.run()
