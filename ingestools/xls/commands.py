import click

from .ingest_request import IngestRequest
from openpyxl.utils.exceptions import InvalidFileException


@click.group()
def xls():
    pass
    """First Command"""


@xls.command('summary')
@click.argument('file')
def xls_summary(file):
    """FILE path to excel file summary"""
    try:
        excel = IngestRequest(file)
        # excel.print_table_summary_real_count()
        excel.print_table_summary()
    except InvalidFileException:
        click.echo("ERROR: File not found or not Excel File!")


@xls.command('show')
def xls_show():
    """Show the Excel file"""
    print('show command')
