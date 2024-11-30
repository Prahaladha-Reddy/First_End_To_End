from src.datascience import logger
from src.datascience.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.datascience.pipeline.data_validation_pipeline import DatavalidationTrainingPipeline
from src.datascience.pipeline.data_transformation_pipeline import DataTransformationTrainingPiprline

from src.datascience.pipeline.model_pipeline import ModelTrainerTrainingPipeline
logger.info('Welcome Custome logger')


STAGE_NAME='Data Ingestion Stage'

try:
  logger.info(f'>> Stage {STAGE_NAME} started >>')
  obj=DataIngestionTrainingPipeline()
  obj.initiate_data_ingestion()
  logger.info(f'>> stage {STAGE_NAME} completed >> \n\nx===x')
except Exception as e:
  logger.exception(e)
  raise e


STAGE_NAME='Model evaluation stage'

if __name__ == '__main__':
    try:
        logger.info(f'>> stage {STAGE_NAME}')
        obj = DatavalidationTrainingPipeline()
        obj.initiate_data_validation()
        logger.info(f'>> stage {STAGE_NAME} completed')
    except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME='Data Transformation Stage'

try:
  logger.info(f'>> Stage {STAGE_NAME} started >>')
  obj=DataTransformationTrainingPiprline()
  obj.initiate_data_transformation()
  logger.info(f'>> stage {STAGE_NAME} completed >> \n\nx===x')
except Exception as e:
  logger.exception(e)
  raise e


STAGE_NAME='Model trainer stage'

try:
  logger.info(f'>> Stage {STAGE_NAME} started >>')
  obj=ModelTrainerTrainingPipeline()
  obj.initiate_model_training()
  logger.info(f'>> stage {STAGE_NAME} completed >> \n\nx===x')
except Exception as e:
  logger.exception(e)
  raise e
