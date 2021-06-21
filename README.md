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

1) Оберните inference вашей модели в rest сервис (3/3)

2) Напишите тест для /predict  (3/3)

3) Напишите скрипт, который будет делать запросы к вашему сервису (2/2)

4) Сделайте валидацию входных данных (3/3)

5) Напишите dockerfile, соберите на его основе образ и запустите локально контейнер(docker build, docker run), внутри контейнера должен запускать сервис, написанный в предущем пункте, закоммитьте его, напишите в readme корректную команду сборки (4/4)

6) Оптимизируйте размер docker image (0/3)

7) опубликуйте образ в https://hub.docker.com/ (2/2)

8) напишите в readme корректные команды docker pull/run, которые должны привести к тому, что локально поднимется на inference ваша модель (1/1)

9) проведите самооценку (1/1)

Итог: 22 балла

