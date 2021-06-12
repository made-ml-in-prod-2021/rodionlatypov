import yaml
from dataclasses import dataclass
from marshmallow_dataclass import class_schema
from .feature_params import FeatureParams


@dataclass()
class PredictionPipelineParams:
	input_data_path: str
	input_model_path: str
	feature_params: FeatureParams
	output_predictions_path: str


PredictionPipelineParamsSchema = class_schema(PredictionPipelineParams)


def read_prediction_pipeline_params(path: str) -> PredictionPipelineParams:
    with open(path, "r") as input_stream:
        schema = PredictionPipelineParamsSchema()
        return schema.load(yaml.safe_load(input_stream))
