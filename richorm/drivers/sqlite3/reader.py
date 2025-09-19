from logging import config
import sqlite3
import yaml

class ConfigFileReader:
    
    def __init__(self, path):
        self.path = path
        
    def get_connection_params(self):
        with open(self.path, "r") as configFile:
            params = yaml.safe_load(configFile)
        return params