from xml.etree.ElementInclude import LimitedRecursiveIncludeError
from ChickenDiseaseClassification.config.configuration import ConfigurationManager
from ChickenDiseaseClassification.components.data_ingestion import DataIngestion
from ChickenDiseaseClassification import logger

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        if not config.is_exists:
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(data_ingestion_config = data_ingestion_config)
            data_ingestion.copy_file()
            data_ingestion.extract_zip_file()
        else:
            logger.info("The folders and necessary files are  already present")