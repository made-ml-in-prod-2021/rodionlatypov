# ML Homework 2: online inference

### Pulling from DockerHub
```bash
docker pull rodionlatypov/online-inference:latest
```
### Running inference
```bash
docker run -p 8000:8000 rodionlatypov/online-inference
```
## Project structure
------------

    ├── data
    │   └──  data.csv     
    │   
    ├── entities                   
    |   ├── __init__.py
    │   ├── request.py
    │   └── response.py
    |
    ├── model                      
    |   └── model.pkl      
    │
    ├── test                    
    │   └── test_app.py             
    │                                     
    ├── validation                 
    |   ├── __init__.py
    │   └── validate.py
    │ 
    ├── Dockerfile
    │
    ├── app.py 
    │
    ├── make_request.py 
    |
    └── requirements.txt
    
------------
## What was done

#### 1) Оберните inference вашей модели в rest сервис (3/3)

См. /app.py

Пример запроса к сервису, запущенному локально, ответ (предсказания модели) в нижнем правом углу:

![Post predict](https://github.com/made-ml-in-prod-2021/rodionlatypov/blob/homework2/online_inference/pics/post_predict.jpg)

#### 2) Напишите тест для /predict  (3/3)

Cм. /test/test_app.py. Покрытие тестами 87%:

![Test coverage](https://github.com/made-ml-in-prod-2021/rodionlatypov/blob/homework2/online_inference/pics/test_coverage.jpg)

#### 3) Напишите скрипт, который будет делать запросы к вашему сервису (2/2)

См. make_request.py. Пример:

![Make requests](https://github.com/made-ml-in-prod-2021/rodionlatypov/blob/homework2/online_inference/pics/requests.jpg)

#### 4) Сделайте валидацию входных данных (3/3)

См. /validation/validate.py. Пример:

![Validation](https://github.com/made-ml-in-prod-2021/rodionlatypov/blob/homework2/online_inference/pics/post_predict_validation.jpg)

#### 5) Напишите dockerfile, соберите на его основе образ и запустите локально контейнер(docker build, docker run), внутри контейнера должен запускать сервис, написанный в предущем пункте, закоммитьте его, напишите в readme корректную команду сборки (4/4)

Сборка контейнера:

![Docker build](https://github.com/made-ml-in-prod-2021/rodionlatypov/blob/homework2/online_inference/pics/docker_build.jpg)

Запуск контейнера:

![Docker run](https://github.com/made-ml-in-prod-2021/rodionlatypov/blob/homework2/online_inference/pics/docker_run.jpg)

Наконец, predict-запрос к докеру:

![Docker post predict](https://github.com/made-ml-in-prod-2021/rodionlatypov/blob/homework2/online_inference/pics/docker_post_predict.jpg)

#### 6) Оптимизируйте размер docker image (0/3)

#### 7) Опубликуйте образ в https://hub.docker.com/ (2/2)

#### 8) Напишите в readme корректные команды docker pull/run, которые должны привести к тому, что локально поднимется на inference ваша модель (1/1)

#### 9) Проведите самооценку (1/1)

Итог: 22 балла

