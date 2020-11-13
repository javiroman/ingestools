import click
from .ingest_request import IngestRequest


@click.group()
def xls():
    pass
    """First Command"""


@xls.command('summary')
@click.argument('file')
def xls_summary(file):
    """FILE path to excel file summary"""
    excel = IngestRequest(file)
    excel.print_sheet_names()


@xls.command('show')
def xls_show():
    """Show the Excel file"""
    print('show command')
