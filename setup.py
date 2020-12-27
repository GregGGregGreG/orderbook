'''
Copyright (C) 2020  Bryant Moscon - bmoscon@gmail.com

Please see the LICENSE file for the terms and conditions
associated with this software.
'''
from os import path
from setuptools import setup, Extension, find_packages
from setuptools.command.test import test as TestCommand
import sys


orderbook = Extension('order_book', sources=['orderbook/orderbook.c'])


def get_long_description():
    repo_dir = path.abspath(path.dirname(__file__))
    markdown = []
    for filename in ("README.md", "CHANGES.md"):
        with open(path.join(repo_dir, filename), encoding="utf-8") as markdown_file:
            markdown.append(markdown_file.read())
    return "\n\n----\n\n".join(markdown)


class Test(TestCommand):
    def run_tests(self):
        import pytest
        errno = pytest.main(['tests/'])
        sys.exit(errno)


setup(
    name='order_book',
    version='0.0.2',
    author="Bryant Moscon",
    author_email="bmoscon@gmail.com",
    description="A fast orderbook implementation, in C, for Python",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    keywords=["market data", "trading"],
    url="https://github.com/bmoscon/orderbook",
    ext_modules=[orderbook],
    packages=find_packages(exclude=['tests*']),
    license='License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    tests_require=["pytest", "requests", "sortedcontainers"],
    cmdclass={'test': Test},
    classifiers=[
        "Intended Audience :: Developers",
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3 :: Only",
    ],
)
