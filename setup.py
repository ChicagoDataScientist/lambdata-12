# setup.py
from setuptools import find_packages, setup
with open("README.md", "r") as fh:
    long_description = fh.read()
setup(
    name="s2t2-lambdata-12",
    version="1.0",
    author="AJ Peterson",
    author_email="sonotony@gmail.com",
    description="For example purposes",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    #license="MIT",
    url="https://github.com/ChicagoDataScientist/lambdata-12",
    #keywords="",
    packages=find_packages() # ["my_lambdata"]
)