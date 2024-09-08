import os
from box.exceptions import BoxValueError
from ChickenDiseaseClassification import logger

import yaml
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import List
import base64

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads the yaml file and returns      
    """
    
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose = True):
    """Creates list of directories

    Args:
        path_to_directories (list): _description_
        verbose (bool, optional): _description_. Defaults to True.
    """
    
    for path in path_to_directories:
        
        os.makedirs(path, exist_ok= True)
        if verbose:
            logger.info(f"created directory at: {path}")
            

def save_json(path:Path, data:dict):
    """save the json data
    """
    
    with open(path, "w") as f:
        json.dump(data, f ,indent = 4)
        
    logger.info(f"json file saved at: {path}")
    
def decode_image(imgstring,filename):
    imgdata = base64.b64decode(imgstring)
    with open(filename, 'wb') as f:
        f.write(imgdata)
        f.close()
            
    

