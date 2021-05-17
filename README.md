# ML project Homework 1

### Train model

```bash
python train_pipeline.py <train-config-path>
```

### Predict with model

```bash
python src/predict_pipeline.py <predict-config-path>
```


## Project structure
------------

    ├── configs                        <- Configuration files.
    │   ├── predict_config.yaml
    │   └── train_config.yaml
    │
    ├── data
    │   ├── data_file.csv              <- Data file.
    │   ├── make_dataset.py            <- Function for splitting datasets into train and test sets.
    |   └── __init__.py
    |
    ├── entities                       <- Parameters for project modules.
    |   ├── __init__.py
    │   ├── feature_params.py
    │   ├── predict_pipeline_params.py
    │   ├── split_params.py
    │   ├── train_params.py
    │   └── train_pipeline_params.py
    |
    ├── features                        <- Features transformer.
    |   ├── __init__.py
    │   └── build_features.py
    |
    ├── logs                           <- Training and prediction log files.
    |   ├── predict.log
    │   └── train.log
    |
    ├── models                         <- Trained models, model predictions, model metrics.
    |   ├── __init__.py
    │   ├── metrics.json
    |   ├── model.pkl
    │   ├── model_fit_predict.py
    │   └── predictions.csv
    │
    ├── notebooks                      <- Jupyter notebooks.
    │   └── Model_HA1.ipynb              
    │                                     
    ├── predict_pipeline.py            <- Prediction pipeline.
    |
    └── train_pipeline.py              <- Train pipeline.
------------

Что сделано:

-2) Назовите ветку homework1 (1/1)

-1) положите код в папку ml_project

0) В описании к пулл реквесту описаны основные "архитектурные" и тактические решения, которые сделаны в вашей работе. В общем, описание что именно вы сделали и для чего, чтобы вашим ревьюерам было легче понять ваш код. (0/2)

1) Выполнение EDA, закоммитьте ноутбук в папку с ноутбуками (0/2)

2) Проект имеет модульную структуру(не все в одном файле =) ) (2/2)

3) использованы логгеры (2/2)

4) написаны тесты на отдельные модули и на прогон всего пайплайна(0/3)

5) Для тестов генерируются синтетические данные, приближенные к реальным (0/3)

6) Обучение модели конфигурируется с помощью конфигов в json или yaml, закоммитьте как минимум 2 корректные конфигурации, с помощью которых можно обучить модель (разные модели, стратегии split, preprocessing) (3/3)

7) Используются датаклассы для сущностей из конфига, а не голые dict (3/3) 

8) Используйте кастомный трансформер(написанный своими руками) и протестируйте его(3/3)

9) Обучите модель, запишите в readme как это предлагается (3/3)

10) напишите функцию predict, которая примет на вход артефакт/ы от обучения, тестовую выборку(без меток) и запишет предикт, напишите в readme как это сделать (3/3)  

13) Проведите самооценку, опишите, в какое колво баллов по вашему мнению стоит оценить вашу работу и почему (1/1) 

Итог: 21 / 30
