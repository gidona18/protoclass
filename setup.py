from pathlib import Path
from setuptools import setup, find_packages

HERE = Path(__file__).parent
README = (HERE / "README.md").read_text()

setup(
    name="protoclass",
    version="0.0.2",
    packages=find_packages(exclude=["tests"]),
    description="Prototype-Oriented Programming in Python",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/jellowfish/protoclass",
    license="Apache-2.0",
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.0",
        "Programming Language :: Python :: 3.1",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    zip_safe=True,
    author="Armando Herrera",
    author_email="mail@jellowfish.com",
)
