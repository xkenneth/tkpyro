from distutils.core import setup
from setuptools import find_packages

setup(name='TkPyro',
      version='0.1',
      description='Xml/Python Tk Run-time',
      author='Kenneth Miller',
      author_email='xkenneth@gmail.com',
      packages = find_packages(),
      install_requires = ['setuptools',
                          ]
     )
