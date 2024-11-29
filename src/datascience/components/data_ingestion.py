import os
import urllib.request as request
from src.datascience import logger
import zipfile
from src.datascience.entity.config_entity import (DataIngestionconfig)


class DataIngestion:
  def __init__(self,config:DataIngestionconfig):
    self.config=config

  def download_file(self):
    if not os.path.exists(self.config.local_data_file):
      filename,header=request.urlretrieve(
        url=self.config.source_URL,
        filename=self.config.local_data_file
      )
      logger.info(f'{filename} downloaded! with following info\n{header}')
    else:
      logger.info(f'File already exists')
  def extract_zip(self):
    unzip_path=self.config.unzip_dir
    os.makedirs(unzip_path,exist_ok=True)
    with zipfile.ZipFile(self.config.local_data_file,'r') as zip_ref:
      zip_ref.extractall(unzip_path)