import pandas as pd
import click
from entities import read_prediction_pipeline_params
import logging
import pickle

from features import make_features
from features.build_features import extract_target, build_transformer

from models import predict_model


APPLICATION_NAME = "ML_IN_PROD_HA1"


logger = logging.getLogger(APPLICATION_NAME)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler = logging.FileHandler("logs/predict.log")
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def predict_pipeline(config_path):
	predict_pipeline_params = read_prediction_pipeline_params(config_path)
	return run_predict_pipeline(predict_pipeline_params)


def run_predict_pipeline(predict_pipeline_params):
	logger.info("Loading data...")

	data = pd.read_csv(predict_pipeline_params.input_data_path)
	logger.info(f"Loaded data shape is {data.shape}")

	logger.info(f"Loading model...")
	model = pickle.load(open(predict_pipeline_params.input_model_path, 'rb'))
	logger.info(f"Loaded model: {model}")

	feature_transformer = build_transformer(predict_pipeline_params.feature_params)
	feature_transformer.fit(data)

	logger.info(f"Preparing features...")
	features = make_features(
		feature_transformer,
		data,
	)
	logger.info(f"Features shape is {features.shape}")

	logger.info(f"Making predictions...")
	predictions = predict_model(model, features)
	logger.info(f"Predictions shape is {predictions.shape}")

	logger.info(f"Saving predictions to {predict_pipeline_params.output_predictions_path}...")
	pd.DataFrame(predictions).to_csv(predict_pipeline_params.output_predictions_path)
	logger.info("Done.")



@click.command(name="predict_pipeline")
@click.argument("config_path")
def main(config_path):
	predict_pipeline(config_path)


if __name__ == '__main__':
	main()
