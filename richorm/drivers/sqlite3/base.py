import sqlite3

from richorm.drivers.base import settings
from richorm.drivers.sqlite3.exceptions import ImproperlyConfigured

settings.read_config()

class ConnectionLayer:
    
    settings_dict = settings.config_dict
    
    def __init__(self):
        self.connection = None
        
    def connect(self):
        """Connect to the database. Assume that the connection is closed."""
        self.check_settings()
        if (
            self.connection is None 
            and 
            self.settings_dict['database']['driver'].lower()=='sqlite3'
        ):
            self.connection = sqlite3.connect(self.settings_dict['database']['name'])
        return self.connection  
    
    def get_cursor(self):
        if self.connection is not None :
            return self.connection.cursor()
        return None
    
    def check_settings(self):
        
        # if False:
        #     pass
        # # raise ImproperlyConfigured(
        # #     "thic setting is imporperly configured. Please Check in config file."
        # # )
        pass


      