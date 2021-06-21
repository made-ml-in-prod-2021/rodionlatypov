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
    └──requirements.txt
    
------------
