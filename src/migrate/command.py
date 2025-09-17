import click

@click.command()
@click.version_option(version="0.1.0")
def cli():
    """Prints a greeting."""
    click.echo("I am coming in WORLD !")