import os
import zipfile
import urllib.request as request
from cnnClassifier import logger
from cnnClassifier.utils.common import get_size
from cnnClassifier.entity.config_entity import DataIngestionConfig
from pathlib import Path
import py7zr



class Dataingestion:
    def __init__(self,config:DataIngestionConfig):
        self.config = config
        
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, header=request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file
            )
            logger.info(f"{filename} : download with following info: \n{header}")
        else:
            logger.info(f"file already exist of size:{get_size(Path(self.config.local_data_file))}")
            
            
    def extract_zip_file(self):
        unzip_path = self.config.unzip_path
        os.makedirs(unzip_path, exist_ok=True)
        with py7zr.SevenZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
        