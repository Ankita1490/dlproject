from ast import Pass
from multiprocessing.spawn import prepare
from xml.dom.pulldom import parseString
from ChickenDiseaseClassification.config.configuration import ConfigurationManager
from ChickenDiseaseClassification.components.prepare_base_model import PrepareBaseModel
from ChickenDiseaseClassification import logger

class PrepareBaseModelPipeline:
    def __init__(self):
        pass
        
    def main(self):
        self.config = ConfigurationManager()
        prepare_base_model_config = self.config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()