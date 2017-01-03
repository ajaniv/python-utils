Python utitilies project
========================

The *python-core-utils* project intent is to help development of python and 
Django applications.  It was initially derived from a collection of 
code snippets used across several projects.

It was developed for both python 2.7 and 3.5

Dependencies
------------

Runtime
^^^^^^^^^^^

* Pillow

Development
^^^^^^^^^^^

* coverage
* flake8
* tox
* virtualenv

Notes
^^^^^

* pandoc can be used to convert from .rst to .md:

  ``pandoc -f rst -t markdown_github -o README.md README.rst``
  
* check-manifest was run from the command line.  Could not get it
  to work from within tox.  There was an error in handling '~'
  with gitconfig when running:
  
  ``git ls-files -z``