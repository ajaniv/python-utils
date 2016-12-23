"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
"""


from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='python-core-utils',
    version='0.2.0',
    description='Python core utility functions',
    long_description=long_description,
    url='https://github.com/ajaniv/python-core-utils',
    author='Amnon Janiv',
    author_email='amnon.janiv@ondalear.com',
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
    ],

    keywords='python core utility functions',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=['Pillow==3.4.2'],
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },
    test_suite='tests'
)
