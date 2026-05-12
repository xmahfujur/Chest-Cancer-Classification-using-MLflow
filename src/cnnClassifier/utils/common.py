import os
import yaml
from box.exceptions import BoxValueError
from cnnClassifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import configBox
from pathlib import Path
from typing import Any
import base64



@ensure_annotations
def read_yaml(path_to_yaml: Path) -> configBox:

    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f'yaml file: {path_to_yaml} loaded successfully')
            return configBox(content)
        
    except BoxValueError:
        raise ValueError('yaml is empty')
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose = True):

    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f'Created directory at: {path}')


@ensure_annotations
def laod_json(path: Path) -> configBox:
    with open(path) as f:
        content = json.load(f)
        return configBox(content)


@ensure_annotations
def save_bin(data: Any, path: Path):
    joblib.dump(value=data, filename=path)





def decodeImage(imgstring, fileName):
    imgdata = base64.b64decode(imgstring)
    with open (fileName, 'wb') as f:
        f.write(imgdata)
        f.close()

def encodeImage(croppedImgePath):
    with open(croppedImgePath, 'rb') as f:
        return base64.b64encode(f.read())
    
     