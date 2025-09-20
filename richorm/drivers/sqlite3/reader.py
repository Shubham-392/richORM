
import yaml
import os

class ConfigFileReader:
    
    def __init__(self, path):
        self.path = path
        
    def get_connection_params(self) -> dict:
        if not os.path.exists(self.path):
            raise FileNotFoundError(
                f"No {self.path} such file exists at this location.\n {'\033[33m'}Try to run 'richorm' command first to generate the file.{'\033[0m'} "
            )
        with open(self.path, "r") as configFile:
            params = yaml.safe_load(configFile)
        return params
    
    
        
        
        
    
        