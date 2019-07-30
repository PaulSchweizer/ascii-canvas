from setuptools import setup
from setuptools import find_packages


with open("README.md") as stream:
    long_description = stream.read()

setup(name='ascii-canvas',
      version='1.3.4',
      author='Paul Schweizer',
      author_email='paulschweizer@gmx.net',
      description='Treat strings like Items on a 2D Canvas.',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='https://github.com/PaulSchweizer/ascii-canvas',
      packages=find_packages(),
      classifiers=[
              'Programming Language :: Python',
              'Programming Language :: Python :: 2.6',
              'Programming Language :: Python :: 2.7',
              'Programming Language :: Python :: 3.4',
              'Programming Language :: Python :: 3.5',
              'Programming Language :: Python :: 3.6',
              'Programming Language :: Python :: 3.7',
        ])
