from ChickenDiseaseClassification.config.configuration import ConfigurationManager
from ChickenDiseaseClassification.components.data_ingestion import DataIngestion
from ChickenDiseaseClassification import logger

STAGE_NAME_01 = "Data Ingestion stage"
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
            
if __name__ == "__main__" :
    try:
        logger.info(f"==== stage {STAGE_NAME_01} started =======")
        data_ingestion = DataIngestionTrainingPipeline()
        data_ingestion.main()
        logger.info(f"======== stage {STAGE_NAME_01} completed ============")
    except Exception as e:
        raise logger.exception(e)