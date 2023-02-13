from setuptools import setup
from os.path import join
import os

project_name = "TradeApp"

requirements = open('requirements.txt').read().splitlines()

setup(
    name=project_name,
    version="0.1.0",
    url="https://github.com/absultan86/TradeApp",
    author="Abdulrahman E. Sultan",
    author_email="absultan86@gmail.com",
    description="Analyse the Stock Market",
    license="MIT",
    install_requires=requirements,
    packages=[
        project_name,
        join(project_name, "todo"),
        join(project_name, "todo"),
        join(project_name, "todo"),
    ],)
