from setuptools import find_packages,setup

setup(
name='mlproject',
version='0.1',
description='A sample Python package',
author='Lalit Singh',
author_email='lalitsingh5522@gmail.com',
packages=find_packages(),
install_requires=['numpy','pandas','seaborn'],
)