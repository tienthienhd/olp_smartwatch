
from flask import request, Flask, jsonify
import numpy as np
import pandas as pd
import pickle
import json
import preprocess
from gesture import get_gestures
# from activity import ActivityRecogniration
#
# model = ActivityRecogniration()
# model.load('activity.model')


app = Flask(__name__)


@app.route('/predict_gesture', methods=['GET', 'POST'])
def predict_gesture():
    if request.method == 'POST':
        data = request.data.decode('utf8')
        data = preprocess.parse_data(data)
        print(data)
        result = get_gestures(data)
        if result is not None:
            return result
        else:
            return 'No gesture'


@app.route('/predict_activity', methods=['GET', 'POST'])
def predict_activity():
    # if request.method == 'POST':
    #     data = request.data.decode('utf8')
    #     data = json.loads(data)
    #     data = data['values'].replace("} {", "}\n{")
    #     return model.get_activity(data_raw=data)
    return 'running'


app.run('0.0.0.0', 5000, debug=True)

