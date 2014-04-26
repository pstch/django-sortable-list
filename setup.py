#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from setuptools import setup

import django_sortable_list

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()
LICENSE = open(os.path.join(os.path.dirname(__file__), 'LICENSE.txt')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-sortable-list',
    version=django_sortable_list.__version__,
    packages=['django_sortable_list'],
    include_package_data=True,
    license=LICENSE,
    description='A MultipleObjectMixin for Django that provides sorting',
    long_description=README,
    url='https://github.com/pstch/django-sortable-list',
    author='Sarah Bird (original), Hugo Geoffroy',
    author_email='hugo@pstch.net',
    install_requires=['django>=1.5'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    test_suite='tests.runtests.runtests',
    tests_require=['Django', 'mock']
)
