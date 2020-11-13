from setuptools import setup, find_packages


setup(
    name='ingestools',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
    ingestools=ingestools.main:init
    ''',
)
