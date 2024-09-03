import os
from pathlib import Path
from ChickenDiseaseClassification.constants import *
from ChickenDiseaseClassification.utils.common import read_yaml, create_directories
from ChickenDiseaseClassification.entity.config_entity import DataIngestionConfig

class ConfigurationManager:
    def __init__(self, config_file_path= CONFIG_FILE_PATH,
                param_file_path = PARAMS_FILE_PATH):
        self.config = read_yaml(config_file_path)
        self.param = read_yaml(param_file_path)
        
        create_directories([self.config.artifact_root])
        
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        
        create_directories([config.root_dir])
        
        data_ingestion_config =DataIngestionConfig(
            root_dir=config.root_dir,
            source_data= config.source_data,
            local_data_file= config.local_data_file,
            unzip_dir= config.unzip_dir
        )
        
        return data_ingestion_config