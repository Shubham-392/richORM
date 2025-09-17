import click
import yaml
import os

@click.command()
@click.version_option(version="0.1.0")
def cli():
    dumping_data = {
        "db":{
            "DRIVER":"adaptor",
            "DB_NAME":"richorm",
            "DB_HOST":"localhost",
            "DB_PORT":3301,
            "DB_PASSWORD":"localhost@password"
        },
        "models":{
            "directory":"path/to/models/directory"
        }
    }
    
    currentDirectory  = os.getcwd()
    with open(f'{currentDirectory}/richorm-config.yml', "w") as configFile:
        yaml.dump(dumping_data, configFile, default_flow_style=False )
    
    