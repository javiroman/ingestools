import click

from .xls import commands as xls
from .db import commands as db


@click.group()
@click.option("--debug", is_flag=True, help='debug application')
@click.version_option(None, "-v", "--version", message="%(version)s")
def init(debug):
    """Ingest Tools Utilities by KEEDIO"""
    pass


# Add main commands
init.add_command(xls.xls)
init.add_command(db.db)
