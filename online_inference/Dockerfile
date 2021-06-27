FROM python:3.8

MAINTAINER rodion latypov <rlatypov@nes.ru>

ENV PATH=./bin.sh:$PATH

COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY ./app.py ./app.py
COPY ./make_request.py ./make_request.py
COPY ./model/model.pkl ./model/model.pkl
COPY ./entities ./entities
COPY ./data ./data
COPY ./validation ./validation

WORKDIR .

ENV PATH_TO_MODEL="model/model.pkl"

CMD ["uvicorn", "app:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
