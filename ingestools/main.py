import click
import configparser

from .xls import commands as xls
from .db import commands as db


@click.group()
@click.option("--debug", is_flag=True, help='debug application')
@click.version_option(None, "-v", "--version", message="%(version)s")
@click.pass_context
def init(ctx, debug):
    """Ingest Tools Utilities by KEEDIO"""

    configfile = configparser.ConfigParser()
    try:
        with open('conf/ingestools.conf') as f:
            configfile.read_file(f)

        ctx.ensure_object(dict)
        ctx.obj['configfile'] = configfile
        ctx.obj['debug'] = debug
    except IOError:
        click.echo("ERROR: Unable to find config file")
        exit(1)


def main():
    init(obj={})


# Add main commands
init.add_command(xls.xls)
init.add_command(db.db)
