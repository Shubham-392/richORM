import os
import yaml

class BaseSettings:
    config_dict = {}
    def read_config(self) -> None :
        home_dir = os.path.expanduser("~")
        CONFIG_DIR = os.path.join(home_dir, '.richorm')
        CONFIG_FILE = os.path.join(CONFIG_DIR,"config.yaml")
        with open(CONFIG_FILE,'r') as config_file:
            settings_dict = yaml.safe_load(config_file)
        BaseSettings.config_dict = settings_dict
        
        
settings = BaseSettings()
            