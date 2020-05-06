from pathlib import Path
from setuptools import setup, find_packages

HERE = Path(__file__).parent
README = ( HERE / 'README.md' ).read_text()

setup(
    name="classless",
    version="0.0.1",
    packages=find_packages(),
    author="Armando Herrera",
    author_email="[email protected]",
    description="TODO",
    long_description=README,
    url="https://github.com/jellowfish/classless",
    license="Apache-2.0"
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    #keywords="TODO",
    #...
    #zip_safe=True,
    #python_requires="3.8",
    #test_suite="TestProto",
)
