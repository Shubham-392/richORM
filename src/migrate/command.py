# package imports 
import click
import yaml
import os

# local imports 
from .dataYAML import dumping_data


ALLOWED_DRIVERS = [
                'mysql', 
                'sqlite', 
                'postgresql', 
                'oracle'
            ]

@click.command()
@click.option('--driver','-d', default="mysql", help='Driver for ORM ')
@click.version_option(version="0.1.0")
def cli( driver:str ):
    
    if driver not in ALLOWED_DRIVERS:
        raise ValueError(
            "This driver is not configured with richORM"
            )
        
    dumping_data["database"]["driver"] = f"{driver}"
    currentDirectory  = os.getcwd()
    
    if not os.path.exists(f'{currentDirectory}/richorm-config.yaml'):
        with open(f'{currentDirectory}/richorm-config.yaml', "w") as configFile:
            yaml.dump(dumping_data, configFile, default_flow_style=False )
            
    else:
        raise FileExistsError(
            "This file already exists in your directory .Please modify that file."
        )
    
    
    
    