from setuptools import find_packages, setup

with open("README.md") as stream:
    long_description = stream.read()

setup(
    name="ascii-canvas",
    version="2.0.1",
    author="Paul Schweizer",
    author_email="paulschweizer@gmx.net",
    description="Treat strings like items on a 2D canvas.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PaulSchweizer/ascii-canvas",
    packages=find_packages(),
    classifiers=["Programming Language :: Python"],
)
