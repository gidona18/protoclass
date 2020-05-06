from pathlib import Path
from setuptools import setup, find_packages

HERE = Path(__file__).parent
README = ( HERE / 'README.md' ).read_text()

setup(
    name='classless',
    version='0.0.1',
    packages=find_packages(exclude=['tests']),
    description='Prototype-Oriented Programming in Python',
    long_description=README,
    url='https://github.com/jellowfish/classless',
    license='Apache-2.0',
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
    ],
    zip_safe=True,
    author='Armando Herrera',
    author_email='[email protected]',
)
