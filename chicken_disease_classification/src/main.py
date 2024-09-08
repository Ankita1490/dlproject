from ChickenDiseaseClassification import logger
from ChickenDiseaseClassification.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from ChickenDiseaseClassification.pipeline.stage_02_prepare_base_model import PrepareBaseModelPipeline
from ChickenDiseaseClassification.pipeline.stage_03_training import ModelTrainingPipeline
from ChickenDiseaseClassification.pipeline.stage_04_evaluation import EvaluationPipeling

STAGE_NAME = "Data Ingestion stage"
STAGE_NAME_02 = "Prepare Base Model Stage"
STAGE_NAME_03 = "Training"
STAGE_NAME_04 = "Evaluation"

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

try:
    logger.info(f"===== stage {STAGE_NAME_03} started =======")
    training = ModelTrainingPipeline()
    training.main()
    logger.info(f"====== stage {STAGE_NAME_03} completed=======")

except Exception as e:
    raise logger.exception(e)


try:
    logger.info(f"======={STAGE_NAME_04} started ======")
    evaluation = EvaluationPipeling()
    evaluation.main()
    logger.info(f"======={STAGE_NAME_04} completed ======")
    
except Exception as e:
    raise logger.exception(e)
