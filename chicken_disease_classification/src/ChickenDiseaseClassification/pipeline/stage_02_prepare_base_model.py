from ast import Pass
from multiprocessing.spawn import prepare
from xml.dom.pulldom import parseString
from ChickenDiseaseClassification.config.configuration import ConfigurationManager
from ChickenDiseaseClassification.components.prepare_base_model import PrepareBaseModel
from ChickenDiseaseClassification import logger

STAGE_NAME_02 = "Prepare Base Model Stage"
class PrepareBaseModelPipeline:
    def __init__(self):
        pass
        
    def main(self):
        self.config = ConfigurationManager()
        prepare_base_model_config = self.config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()
        
if  __name__ == "__main__":
    try:
        logger.info(f"==== stage {STAGE_NAME_02} started =======")
        prepare_base_model = PrepareBaseModelPipeline()
        prepare_base_model.main()
        logger.info(f"======== stage {STAGE_NAME_02} completed ============")
    except Exception as e:
        raise logger.exception(e)
    