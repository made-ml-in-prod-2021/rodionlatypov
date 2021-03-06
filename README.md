# ML Homework 2: online inference

### Pulling from DockerHub
```bash
docker pull rodionlatypov/online-inference:latest
```
### Running inference
```bash
docker run -p 8000:8000 rodionlatypov/online-inference:latest
```
### Docker build
```bash
docker build -t rodionlatypov/online-inference:latest .
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

См. /validation/validate.py. Пример работающей валидации:

![Validation](https://github.com/made-ml-in-prod-2021/rodionlatypov/blob/homework2/online_inference/pics/post_predict_validation.jpg)

#### 5) Напишите dockerfile, соберите на его основе образ и запустите локально контейнер (4/4)

См. /Dockerfile 

Сборка контейнера:

![Docker build](https://github.com/made-ml-in-prod-2021/rodionlatypov/blob/homework2/online_inference/pics/docker_build.jpg)

Запуск контейнера:

![Docker run](https://github.com/made-ml-in-prod-2021/rodionlatypov/blob/homework2/online_inference/pics/docker_run.jpg)

Predict-запрос к запущенному докеру (IP адрес докер-машины по дефолту 192.168.99.100). Ответ в формате [{id: , predicted target:}]:

![Docker post predict](https://github.com/made-ml-in-prod-2021/rodionlatypov/blob/homework2/online_inference/pics/docker_post_predict.jpg)

Predict-запрос к контейнеру, собранному из уменьшенного (оптимизированного) образа:

![Docker post predict to minimised image](https://github.com/made-ml-in-prod-2021/rodionlatypov/blob/homework2/online_inference/pics/test_to_minimised_image.jpg)

Get status запрос к докеру:

![Docker get status](https://github.com/made-ml-in-prod-2021/rodionlatypov/blob/homework2/online_inference/pics/docker_get_status.jpg)

#### 6) Оптимизируйте размер docker image (3/3)

Для того чтобы сократить размер образа, я:
1) Откатил библиотеки до более старых версий, но так, чтобы все необходимые функции в ней были, пришлось помучиться с scikit-learn
2) Удалил лишние директории из докерфайла, которые не нужны для корректной работы запросов
3) Поменял FROM python:3.8 на FROM python:3.7-slim-stretch в докерфайле

**См. результат здесь:**
**https://hub.docker.com/r/rodionlatypov/online-inference/tags?page=1&ordering=last_updated**

Результат оптимизации (сокращение размера больше, чем в 2 раза):

![Optimised image](https://github.com/made-ml-in-prod-2021/rodionlatypov/blob/homework2/online_inference/pics/resized_image.jpg)

#### 7) Опубликуйте образ в https://hub.docker.com/ (2/2)

https://hub.docker.com/r/rodionlatypov/online-inference/tags?page=1&ordering=last_updated

#### 8) Напишите в readme корректные команды docker pull/run, которые должны привести к тому, что локально поднимется на inference ваша модель (1/1)

```bash
docker pull rodionlatypov/online-inference:latest
docker run -p 8000:8000 rodionlatypov/online-inference:latest
```

#### 9) Проведите самооценку (1/1)

Итог: 22 балла

