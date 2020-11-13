from setuptools import setup, find_packages

setup(
    name='ingestools',
    version='0.0.1',
    author="Javi Roman",
    author_email="jroman@keedio.com",
    description="Ingest Tools Utilities",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'JayDeBeApi',
        'openpyxl',
    ],
    entry_points='''
        [console_scripts]
        ingestools=ingestools.main:init
    ''',
)
