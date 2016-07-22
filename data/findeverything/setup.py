#coding:UTF-8
import codecs
import os,sys
from distutils.util import get_platform
try:
    from setuptools import setup
except:
    from distutils.core import setup

def read(fname):
    return codecs.open(os.path.join(os.path.dirname(__file__), fname)).read()

AUTHOR = "yejinlei"
EMAIL = "4010896@qq.com"
LICENSE = "BSD"
CLASS = [
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ]

DES = ("find keyword from files, "
            "needs everything, it's important!")
LONG_DES = read('README.rst')
NAME = "findeverything"
VERSION = "0.1.1"
KEYWORD = "find grep es everything"
URL = "https://github.com/yejinlei/about-python/tree/master/data/findeverything"
REQUIRES = ['futures']

setup(
    name = NAME,
    version = VERSION,
    keywords = KEYWORD,
    packages  = ['findeverything'],
    description = DES,
    long_description = LONG_DES,
    author = AUTHOR,
    author_email = EMAIL,
    url = URL,
    install_requires = REQUIRES,
    platforms = get_platform(),
    license = LICENSE,
    zip_safe = False,
    classifiers = CLASS,
)