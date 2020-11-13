import click

from .xls import commands as xls
from .db import commands as db


@click.group()
def init():
    pass


# Add main commands
init.add_command(xls.xls)
init.add_command(db.db)
