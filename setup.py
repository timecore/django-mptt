#!/usr/bin/env python
from setuptools import setup, find_packages

version = '0.4.0-CORE'
setup(
    name = 'django-mptt',
    description = '''Utilities for implementing Modified Preorder Tree Traversal
        with your Django Models and working with trees of Model instances.''',
    version = version,
    author = 'Jonathan Buchanan',
    author_email = 'craig.ds@gmail.com',
    url = 'http://github.com/django-mptt/django-mptt',
    test_suite="mptt.tests.test_runner.run_tests",
    packages=find_packages(exclude=['mptt.tests']),
    package_data={'mptt': ['templates/admin/*']},
    classifiers = ['Development Status :: 4 - Beta',
                   'Environment :: Web Environment',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Utilities'],
)
