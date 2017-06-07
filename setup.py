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
      license='Apache License 2.0',
      zip_safe = False,
      py_modules=['nose_todo_plugin']
      entry_points = {
        'nose.plugins.0.10': [ 'nose_todo_plugin = nose_todo_plugin:TodoWarningPlugin' ]
      },
     )
