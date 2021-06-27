import json
import requests

import pandas as pd
from entities import Request

DATA_PATH = 'data/data.csv'


if __name__ == '__main__':
    data = pd.read_csv(DATA_PATH).drop('target', axis=1)
    request_data = data.to_dict(orient='records')

    response = requests.post(
        'http://0.0.0.0:8000/predict',
        json.dumps(request_data)
    )

    print(response.json())
