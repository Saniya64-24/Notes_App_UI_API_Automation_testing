import yaml

def get_config():
    with open("config/config.yaml") as f:
        return yaml.safe_load(f)
    

#   dev ,stagong .qa, uat