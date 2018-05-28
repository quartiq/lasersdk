#!/usr/bin/env python3

import sys
from setuptools import setup
from setuptools import find_packages


setup(
    name="lasersdk",
    version="1.1.0",
    description="ARTIQ driver for TOPTICA Laser SDK",
    long_description=open("README.rst").read(),
    author="Robert Jördens",
    author_email="rj@quartiq.de",
    url="https://github.com/quartiq/lasersdk",
    download_url="https://github.com/quartiq/lasersdk",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "aqctl_laser = lasersdk.aqctl_laser:main",
        ],
    },
    test_suite="lasersdk.test",
    license="LGPLv3+",
)
