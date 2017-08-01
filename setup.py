#!/usr/bin/env python
from __future__ import print_function
from setuptools import setup, find_packages
import codecs
import sys

setup(
        name="test_jieba",
        version="0.1.1",
        author="donttal",
        author_email="3233795485@qq.com",
        description="后台链接进去，输出分词结果",
        long_description=codecs.open("README.md", "r", "utf-8"),
        license="MIT",
        url="git@github.com:donttal/test_jieba.git",
        packages=['work'],

);
