# package imports
from importlib.machinery import EXTENSION_SUFFIXES
from operator import contains
import os
import re
 
# local imports
from richorm.migrate.data_yaml import SQLITE3_DBCONFIG

def _prepare_config(params:dict) -> list :
    params_keys = list(params.keys())
    SQLITE3_CONFIG_KEYS = list(SQLITE3_DBCONFIG.keys())
    missing_params = [key for key in SQLITE3_CONFIG_KEYS if key not in params_keys]
            
    return  missing_params
            
            