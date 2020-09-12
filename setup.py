"""This setup script packages pyblish-photoshop."""

import importlib
import os

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

version_file = os.path.abspath("pyblish_photoshop/version.py")
version_mod = importlib.import_module("pyblish_photoshop.version")
version = version_mod.version

classifiers = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
    "Operating System :: Microsoft :: Windows",
    "Operating System :: Microsoft :: Windows :: Windows 10",
    "Programming Language :: Python :: 3 :: Only",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Topic :: Utilities"
]

setup(
    name="pyblish-photoshop",
    version=version,
    packages=find_packages(),
    url="https://github.com/pyblish/pyblish-photoshop",
    license="LGPL",
    author="Abstract Factory and Contributors",
    author_email="marcus@abstractfactory.io",
    description="Maya Pyblish package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    zip_safe=False,
    classifiers=classifiers,
    package_data={"pyblish_photoshop": ["plugins/*.py"]},
    install_requires=[
        "pyblish-base>=1.5.3"
        "pyblish_qml",
        "click>=7.0"
    ],
    entry_points={
        "console_scripts": ["pyblish-photoshop = pyblish_photoshop.app:cli"]
    },
)
