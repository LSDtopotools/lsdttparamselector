#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['ipykernel','ipython','ipywidgets']

setup_requirements = ['pytest-runner', 'ipykernel','ipython','ipywidgets']

test_requirements = ['pytest>=3', 'ipykernel','ipython','ipywidgets' ]

setup(
    author="Simon M Mudd",
    author_email='simon.m.mudd@ed.ac.uk',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="A small package using ipython widgets that allows users to select parameters from menus. These can be passed to another object in lsdviztools to create a driver file for the lsdtopotools command line tools.",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='lsdttparamselector',
    name='lsdttparamselector',
    packages=find_packages(include=['lsdttparamselector', 'lsdttparamselector.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/simon-m-mudd/lsdttparamselector',
    version='0.1.0',
    zip_safe=False,
)
