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
    #install_requires = ['IMDbPY', 'beautifulsoup'],
    dependency_links = [
        "http://www.crummy.com/software/BeautifulSoup/bs4/download/4.3/beautifulsoup4-4.3.2.tar.gz",
        "https://bitbucket.org/alberanid/imdbpy/get/5.0.tar.gz"
    ],
    long_description=read('README.md'),
)