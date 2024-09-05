import os
from pathlib import Path
from ChickenDiseaseClassification.constants import *
from ChickenDiseaseClassification.utils.common import read_yaml, create_directories
from ChickenDiseaseClassification.entity.config_entity import DataIngestionConfig, PrepareBaseModelConfig, PrepareCallbacksConfig

class ConfigurationManager:
    def __init__(self, config_file_path= CONFIG_FILE_PATH,
                param_file_path = PARAMS_FILE_PATH):
        self.config = read_yaml(config_file_path)
        self.param = read_yaml(param_file_path)
        self.is_exists =os.path.exists(self.config.artifact_root)
        if not self.is_exists:
            create_directories([self.config.artifact_root])
        
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        is_exists = os.path.exists(config.root_dir)
        if not is_exists:
            create_directories([config.root_dir])
        
        data_ingestion_config =DataIngestionConfig(
            root_dir=config.root_dir,
            source_data= config.source_data,
            local_data_file= config.local_data_file,
            unzip_dir= config.unzip_dir
        )
        
        return data_ingestion_config
    
    def get_prepare_base_model_config(self) -> PrepareBaseModelConfig:
        config = self.config.prepare_base_model
        is_exists = os.path.exists(config.root_dir)
        if not is_exists:
            create_directories([config.root_dir])
        
        prepare_base_model_config = PrepareBaseModelConfig(
            root_dir = Path(config.root_dir),
            base_model_path= Path(config.base_model_path),
            updated_base_model_path= Path(config.updated_base_model_path),
            params_image_size = self.param.IMAGE_SIZE,
            params_learning_rate= self.param.LEARNING_RATE,
            params_include_top = self.param.INCLUDE_TOP,
            params_weights = self.param.WEIGHTS,
            params_classes=self.param.CLASSES
            
        )
        
        return prepare_base_model_config
    
    def get_prepare_callback_config(self) -> PrepareCallbacksConfig:
        config = self.configs.prepare_callbacks
        create_directories([
            Path(config.checkpoint_model_filepath), 
            Path(config.tensorboard_root_log_dir)
        ])
            
        prepare_callback_config = PrepareCallbacksConfig(
            root_dir= Path(config.root_dir),
            checkpoint_model_filepath= Path(config.checkpoint_model_filepath),
            tensorboard_root_log_dir= Path(config.tensorboard_root_log_dir)
            
        )
        return prepare_callback_config