import os

from setuptools import setup

version = '0.10'

setup(name='noseplugins',
      version=version,
      description='',
      long_description=open("README.md").read(),
      classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python"],
      keywords='web services',
      author='Quintagroup, Ltd.',
      author_email='info@quintagroup.com',
      url='https://github.com/openprocurement/noseplugins',
      py_modules = ['nose_todo_plugin'],
      license='Apache License 2.0',
      zip_safe = False,
      entry_points = {
        'todo': [ 'todo = nose_todo_plugin:TodoWarningPlugin' ]
      },
     )
