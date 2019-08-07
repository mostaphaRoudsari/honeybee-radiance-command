import re
import setuptools
import sys

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="honeybee-radiance-command",
    use_scm_version = True,
    setup_requires=['setuptools_scm'],
    author="Ladybug Tools",
    author_email="info@ladybug.tools",
    description="Honeybee wrapper around Radiance commands which is used by honeybee-radiance",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ladybug-tools/honeybee-radiance-command",
    packages=setuptools.find_packages(exclude=["tests"]),
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: CPython",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent"
    ],
)