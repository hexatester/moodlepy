#!/usr/bin/env python
"""The setup and build script for the moodlepy library. Thank you python-telegram-bot"""

import codecs
import os
from setuptools import setup, find_packages


def requirements():
    """Build the requirements list for this project"""
    requirements_list = []

    with open("requirements.txt") as requirements:
        for install in requirements:
            requirements_list.append(install.split(";")[0].strip())

    return requirements_list


__version__ = ""
packages = find_packages(exclude=["tests*"])
requirements = requirements()

with codecs.open("README.md", "r", "utf-8") as fd:
    fn = os.path.join("moodle", "version.py")
    with open(fn) as fh:
        code = compile(fh.read(), fn, "exec")
        exec(code)
    setup(
        name="moodlepy",
        version=__version__,
        author="Habib Rohman",
        author_email="habibrohman@protonmail.com",
        license="MIT",
        url="https://github.com/hexatester/moodlepy",
        description="Python wrapper for moodle web service.",
        long_description=fd.read(),
        classifiers=[
            "Development Status :: 4 - Beta",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
            "Topic :: Software Development :: Libraries :: Python Modules",
            "Topic :: Education",
            "Programming Language :: Python",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
        ],
        packages=packages,
        install_requires=requirements,
        entry_points={"console_scripts": ["moodle=moodle.__main__:main"]},
    )
