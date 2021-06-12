import pandas as pd
import click
import logging
from entities import read_training_pipeline_params
from data import split_train_val_data

from features import make_features
from features.build_features import extract_target, build_transformer

from models import train_model, predict_model, evaluate_model, serialize_model

import json

APPLICATION_NAME = "ML_IN_PROD_HA1"


logger = logging.getLogger(APPLICATION_NAME)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler = logging.FileHandler("logs/train.log")
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def train_pipeline(config_path):
	training_pipeline_params = read_training_pipeline_params(config_path)
	return run_train_pipeline(training_pipeline_params)


def run_train_pipeline(training_pipeline_params):
	logger.info(f"Loading data...")
	df = pd.read_csv(training_pipeline_params.input_data_path)
	logger.info(f"Data shape is {df.shape}")

	logger.info(f"Splitting dataset into train and test sets...")

	train_df, val_df = split_train_val_data(
		df, training_pipeline_params.splitting_params
	)

	train_target = train_df[training_pipeline_params.feature_params.target_col]
	val_target = val_df[training_pipeline_params.feature_params.target_col]
	train_df = train_df.drop(training_pipeline_params.feature_params.target_col, 1)
	val_df = val_df.drop(training_pipeline_params.feature_params.target_col, 1)

	logger.info(f"Train sample shape is {train_df.shape}")
	logger.info(f"Test sample shape is {val_df.shape}")

	transformer = build_transformer(training_pipeline_params.feature_params)
	transformer.fit(train_df)

	logger.info(f'Transforming train features...')

	train_features = make_features(transformer, train_df)
	logger.info(f"train_features.shape is {train_features.shape}")

	logger.info(f"Building the model...")

	model = train_model(
		train_features, train_target, training_pipeline_params.train_params
	)

	logger.info(f"Transforming test features...")

	val_features = make_features(transformer, val_df)
	logger.info(f"val_features.shape is {val_features.shape}")

	logger.info(f"Making predictions...")
	predicts = predict_model(
		model,
		val_features,
	)

	logger.info(f"Calculating metrics...")
	metrics = evaluate_model(
		predicts,
		val_target,
	)

	logger.info(f"Accuracy score: {metrics['accuracy']}, ROC_AUC score: {metrics['roc_auc']}.")

	with open(training_pipeline_params.metric_path, "w") as metric_file:
		json.dump(metrics, metric_file)

	path_to_model = serialize_model(model, training_pipeline_params.output_model_path)

	logger.info("Done.")

	return path_to_model, metrics




@click.command(name="train_pipeline")
@click.argument("config_path")
def main(config_path):
	train_pipeline(config_path)


if __name__ == '__main__':
	main()
