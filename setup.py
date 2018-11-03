from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name = 'pyhokchew',
    version = '0.1.1.dev',
    description = 'Doing Hokchew (Fuzhou) linguistics with Python.',
    long_description = long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/MindongLab/PyHokchew',
    author='Radium Zheng',
    packages = find_packages(exclude=['contrib','docs','tests'])
)