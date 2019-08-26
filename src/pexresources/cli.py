import click
import importlib_resources

import pexresources


@click.command()
def cli():
    resource = importlib_resources.read_text(pexresources, 'resource')
    print(resource.strip())
