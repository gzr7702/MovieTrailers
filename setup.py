import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "MovieTrailers",
    version = "0.0.4:",
    author_email = "rgraziano.gzr7702@gmail.com",
    description = ("Creates a page to display movie information."),
    install_requires = ['IMDbPY', 'beautifulsoup'],
    long_description=read('README.md'),
)