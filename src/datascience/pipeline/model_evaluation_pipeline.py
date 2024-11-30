
from src.datascience.config.configuration import ConfigurationManager
from src.datascience import logger
from src.datascience.components.model_evalation import ModelEvaluation


STAGE_NAME='Model Evaluation stage'

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def initiate_model_evaluation(self):
      try:
          config = ConfigurationManager()
          model_evaluation_config = config.get_model_evaluation_config()
          model_evaluation = ModelEvaluation(config=model_evaluation_config)
          model_evaluation.log_into_mlflow()
      except Exception as e:
          raise e