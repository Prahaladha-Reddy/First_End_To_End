from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.data_transformation import DataTransformation
from src.datascience import logger
from pathlib import Path

STAGE_NAME='Data Transformation'

class DataTransformationTrainingPiprline:
  def __init__(self):
   pass
  def  initiate_data_transformation(self):
    try:
      with open(Path('artifacts/data_validation/status.txt'),'r') as f:
        status=f.read().split(' ')[-1]
      if status=="True":
        config=ConfigurationManager()
        data_transformation_config=config.gat_data_transformation_config()
        data_transformation=DataTransformation(data_transformation_config)
        data_transformation.train_test_splitting()
      else :
        raise Exception("The schema does't match")
    except Exception as e:
      print(e)