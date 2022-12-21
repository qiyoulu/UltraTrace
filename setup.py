from setuptools import setup, find_namespace_packages
from fontTools.ttLib import TTFont
import zipfile
import requests


def get_requirements(path):
    with open(path) as f:
        return list(filter(lambda s: len(s) > 0, (get_requirement(l) for l in f)))


def get_requirement(line):
    r, *_ = line.split("#")
    return r.strip().split()


def get_font():
    url = 'http://sourceforge.net/projects/dejavu/files/dejavu/2.37/dejavu-fonts-ttf-2.37.zip'
    r = requests.get(url, allow_redirects=True)
    open('dejavu.zip', 'wb').write(r.content)
    with zipfile.ZipFile('dejavu.zip', 'r') as zip_ref:
        zip_ref.extractall('/Library/Fonts/')


setup(
    name="ultratrace",
    author="Jonathan Washington",
    author_email="jwashin1@swarthmore.edu",
    version="0.9.1",
    packages=find_namespace_packages(
        #include=["ultratrace2.*"], exclude=["ultratrace.*"]
        include=["ultratrace.*"], exclude=["ultratrace2.*"]
    ),
    description="A tool for manually annotating ultrasound tongue imaging (UTI) data",
    install_requires=get_requirements("requirements.txt"),
    entry_points={
        "console_scripts": [
            "ultratrace = ultratrace.__main__:main"
        ]
    },
    extras_require={
        "dev": [
            "flake8",
            "black",
            "mypy",
            "pytest",
            "numpy-stubs @ git+https://github.com/numpy/numpy-stubs.git@master",
            "pytest-cov",
            "pytest-mock",
            "boto3",
            "mypy-boto3-s3",
        ]
    },
    get_font()
)
