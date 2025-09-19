# package imports 
import click
import yaml
import os
import copy

# local imports 
from .dataYAML import dumping_data
from richorm.drivers.sqlite3.reader import ConfigFileReader


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
        ALLOWED_DRIVERS_local = copy.deepcopy(ALLOWED_DRIVERS)
        
        if driver not in ALLOWED_DRIVERS_local:
            raise ValueError(
                "This driver is not configured with richORM"
                )
            
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
def read(config_path:str):
    _wrapper_instance = ConfigFileReader(config_path)
    config_data = _wrapper_instance.get_connection_params()
    