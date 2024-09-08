from ChickenDiseaseClassification.config.configuration import ConfigurationManager
from ChickenDiseaseClassification.components.evaluation import Evaluation
from ChickenDiseaseClassification import logger

STAGE_NAME_04 = "Evaluation"
class EvaluationPipeling:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        val_config = config.get_validation_config()
        evaluation =Evaluation(val_config)
        evaluation.evalution()
        evaluation.save_score()
        
if __name__ == "__main__":
    try:
        logger.info(f"======={STAGE_NAME_04} started ======")
        evaluation = EvaluationPipeling()
        evaluation.main()
        logger.info(f"======={STAGE_NAME_04} completed ======")
        
    except Exception as e:
        raise logger.exception(e)   