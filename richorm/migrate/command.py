# package imports 
from logging import config
import click
import yaml
import os
import copy

# local imports 
from .data_yaml import dumping_data, SQLITE3_DBCONFIG
from richorm.drivers.sqlite3.reader import ConfigFileReader
from richorm.drivers.sqlite3.utils import _validate_sqlite3_config
from richorm.drivers.sqlite3.base import BaseDriverWrapper

ALLOWED_DRIVERS = [
                'mysql', 
                'sqlite3', 
                'postgresql', 
                'oracle'
            ]


@click.group(invoke_without_command=True)
@click.option('--driver','-d', default="sqlite3", help='Driver for ORM ')
@click.version_option(version="0.1.0")
@click.pass_context
def cli ( 
        ctx,
        driver:str 
    )   :
     if ctx.invoked_subcommand is None:
        if driver not in ALLOWED_DRIVERS:
            raise ValueError(
                "This driver is not configured with richORM"
                )
        if driver =="sqlite3":
            dumping_data["database"] = SQLITE3_DBCONFIG
        dumping_data["database"]["driver"] = f"{driver}"
        current_directory  = os.getcwd()
        config_filename = "richorm-config.yaml"
        config_path = os.path.join(current_directory, config_filename)
        
        if not os.path.exists(config_path):
            with open(config_path,"w") as config_file:
                yaml.dump(
                    dumping_data, 
                    config_file, 
                    default_flow_style=False 
                )
                
            click.echo(
                    f'Configuration file for richORM is created at {config_path}'
            )
                
        else:
            raise FileExistsError(
                    f"The file {config_path} already exists in your directory .Please modify that file."
            )
    
@cli.command()
@click.argument('config_path')
def read(
        config_path:str
    ):
    _wrapper_instance = ConfigFileReader(config_path)
    config_data = _wrapper_instance.get_connection_params()
    database_config = config_data['database']
    db_validation = _validate_sqlite3_config(database_config)
    if not db_validation:
        raise ValueError(
            f'Please check configuration file of ORM for sqlite3.\n Must contain the "name" and "driver" in config of database.  '
        )
    
       