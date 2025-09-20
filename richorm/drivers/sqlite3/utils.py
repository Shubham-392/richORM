# package imports
from importlib.machinery import EXTENSION_SUFFIXES
from operator import contains
import os
import re
 
# local imports
from richorm.migrate.data_yaml import SQLITE3_DBCONFIG

def _validate_sqlite3_config(params:dict) :
    if params == SQLITE3_DBCONFIG:
        db_file_name = params['name']
        root, extension = os.path.splitext(db_file_name)
        pattern = r'^\.[a-zA-Z0-9_-]+$'
        if not bool(re.match(pattern, extension)):
            raise ValueError(
                f"Invalid extension for sqlite3 database"
            )
            
        return True
    else:
        return False