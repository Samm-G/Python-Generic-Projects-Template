import os
import logging
import json
import yaml


# Create directories, given a list of paths..
def create_directories(path_to_directories: list) -> None:
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        logging.info(f"created directory at: {path}")
    return None


# Read '.YAML' into a dict..
def read_yaml(path_to_yaml: str) -> dict:
    with open(path_to_yaml) as yaml_file:
        content = yaml.safe_load(yaml_file)
    logging.info(f"yaml file: {path_to_yaml} loaded successfully")
    return content


# Save '.YAML' from a dict..
def save_yaml(path_to_yaml: str, dictionary: dict) -> None:
    with open(path_to_yaml, "w") as yaml_file:
        yaml.dump(dictionary, yaml_file)
    logging.info(f"yaml file: {path_to_yaml} saved successfully")
    return None


# Load '.JSON' as dict.. (Usually used for Metrics data)
def load_json(path: str) -> dict:
    with open(path, "r") as f:
        content = json.load(f)
    logging.info(f"json file {path} loaded successfully")
    return content


# Save dict as '.JSON'.. (Usually used for Metrics data)
def save_json(path: str, data: dict) -> None:
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    logging.info(f"json file {path} saved successfully")
    return None
