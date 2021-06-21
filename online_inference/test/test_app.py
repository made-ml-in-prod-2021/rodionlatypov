import pytest
import json
from fastapi.testclient import TestClient

from app import app
from entities import Request

def test_main_endpoint_correct():
	with TestClient(app) as client:
		response = client.get('/')
		assert 200 == response.status_code


def test_status_endpoint_correct():
	with TestClient(app) as client:
		response = client.get("/status")
		expected_response = 'Model is ready: True.'
		assert expected_response == response.json()
		assert 200 == response.status_code


@pytest.fixture()
def test_data():
    data = [Request(age=18, sex=1, cp=0, trestbps=100, chol=220, fbs=0, restecg=0, thalach=50, exang=0, oldpeak=0.0, slope=0, ca=0, thal=0)]
    return data


def test_predict_endpoint_correct(test_data):
	with TestClient(app) as client:
		response = client.post('/predict', data=json.dumps([x.__dict__ for x in test_data]))
		assert 200 == response.status_code
		assert len(response.json()) == len(test_data)
