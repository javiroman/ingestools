import click


@click.group()
def db():
    pass
    """First Command"""


@db.command('connection')
def db_connection():
    """Commands for WP"""
    click.echo("Command 1 Group 2")


@db.command('evaluate')
@click.option("--test", help="This is the test option")
def db_evaluate():
    """Test Install for WP"""
    print('Installing...')
