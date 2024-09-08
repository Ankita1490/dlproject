import tensorflow as tf
from pathlib import Path
from ChickenDiseaseClassification.utils.common import save_json
from ChickenDiseaseClassification.config.configuration import EvaluationConfig

class Evaluation:
    def __init__(self, config: EvaluationConfig):
        self.config = config
        
    def valid_generator(self):
        detagenerator_kwargs = dict(
            rescale = 1./255,
            validation_split = 0.30
        )
        
        dataflow_kwargs = dict(
            target_size = self.config.params_image_size[:-1],
            batch_size = self.config.params_batch_size,
            interpolation = "bilinear"
        )
        
        valid_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
            **detagenerator_kwargs
        )
        
        self.valid_generator = valid_datagenerator.flow_from_directory(
            directory = self.config.training_data,
            subset = "validation",
            shuffle = False,
            **dataflow_kwargs
        )
        
    @staticmethod
    def load_model(path:Path)-> tf.keras.Model:
        return tf.keras.models.load_model(path)
    
    def evalution(self):
        model = self.load_model(self.config.path_of_model)
        self.valid_generator()
        self.score = model.evaluate(self.valid_generator)
        
    def save_score(self):
        scores = {'loss': self.score[0], "accuracy": self.score[1]}
        save_json(path = Path("scores.json"), data = scores)