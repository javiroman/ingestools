import click


@click.group()
def xls():
    pass
    """First Command"""


@xls.command('summary')
def xls_summary():
    """Commands for WP"""
    click.echo("Command 1 Group 1")


@xls.command('show')
@click.option("--test", help="This is the test option")
def xls_show():
    """Test Install for WP"""
    print('Installing...')
