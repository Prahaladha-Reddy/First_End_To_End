from src.datascience import logger
from src.datascience.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
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