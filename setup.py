#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    # TODO: put package requirements here
    'CoolProp',
    'numpy'
]

setup_requirements = [
    'pytest-runner',
    # TODO(pierrebarroca): put setup requirements (distutils extensions, etc.) here
]

test_requirements = [
    'pytest'
    # TODO: put package test requirements here
]

setup(
    name='python_ph_diagrams',
    version='0.1.0',
    description="Python package to create nice ph diagrams with CoolProp.",
    long_description=readme + '\n\n' + history,
    author="Pierre Barroca",
    author_email='pi.barroca@gmail.com',
    url='https://github.com/pierrebarroca/python_ph_diagrams',
    packages=find_packages(include=['python_ph_diagrams']),
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='python_ph_diagrams',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
