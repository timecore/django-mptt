"""
Django mptt setup file
"""
import os
from setuptools import setup, find_packages

version = "0.3.2-CORE"

setup(
    name = 'django-mptt',
    description = '''Utilities for implementing Modified Preorder Tree Traversal
        with your Django Models and working with trees of Model instances.''',
    version = version,
    author = 'Jonathan Buchanan',
    author_email = 'craig.ds@gmail.com',
    url = 'http://github.com/django-mptt/django-mptt',
    install_requires=[
        'Django',
    ],
    test_suite="mptt.tests.test_runner.run_tests",
    packages=find_packages(),
    classifiers = ['Development Status :: 4 - Beta',
                   'Environment :: Web Environment',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Utilities'],
)
