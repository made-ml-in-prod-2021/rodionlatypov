import pickle
import pandas as pd
import os, json
import uvicorn
from fastapi import FastAPI, HTTPException
from typing import List, Optional
from sklearn.pipeline import Pipeline

from entities import Request, Response
from validation import check_data_validity

PATH_TO_MODEL = 'model/model.pkl'
pipeline: Optional[Pipeline] = None

app = FastAPI()


def make_prediction(request: List[Request], pipeline: Pipeline) -> List[Response]:
	data = pd.DataFrame(x.__dict__ for x in request)
	ids = [int(x) for x in data.index]
	predictions = pipeline.predict(data)

	return [Response(id=int(id_), target=int(target_)) for id_, target_ in zip(ids, predictions)]


@app.get('/')
def main():
    return 'Online prediction initiation'


@app.on_event('startup')
def load_model():
    model_path = os.getenv('PATH_TO_MODEL', default=PATH_TO_MODEL)
    if model_path is None:
        err = f'PATH_TO_MODEL {model_path} is None'
        raise RuntimeError(err)
    global pipeline
    with open(model_path, 'rb') as f:
        pipeline = pickle.load(f)


@app.get('/status')
def status():
    return f'Model is ready: {pipeline is not None}.'


@app.api_route("/predict", response_model=List[Response], methods=['POST'])
def predict(request: List[Request]):
    for data in request:
        is_valid, error_message = check_data_validity(data)
        if not is_valid:
            raise HTTPException(status_code=400, detail=error_message)
    return make_prediction(request, pipeline)



if __name__ == "__main__":
	uvicorn.run('app:app', host='0.0.0.0', port=8000)
