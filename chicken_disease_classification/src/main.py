from ChickenDiseaseClassification import logger
from ChickenDiseaseClassification.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from ChickenDiseaseClassification.pipeline.stage_02_prepare_base_model import PrepareBaseModelPipeline

STAGE_NAME = "Data Ingestion stage"
STAGE_NAME_02 = "Prepare Base Model Stage"

try:
    logger.info(f"==== stage {STAGE_NAME} started =======")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f"======== stage {STAGE_NAME} completed ============")
except Exception as e:
    raise logger.exception(e)



try:
    logger.info(f"==== stage {STAGE_NAME_02} started =======")
    prepare_base_model = PrepareBaseModelPipeline()
    prepare_base_model.main()
    logger.info(f"======== stage {STAGE_NAME_02} completed ============")
except Exception as e:
    raise logger.exception(e)
