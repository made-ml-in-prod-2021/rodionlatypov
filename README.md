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
