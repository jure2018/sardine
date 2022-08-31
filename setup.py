#!/usr/bin/env python3

from setuptools import find_namespace_packages, setup
import pathlib

here = pathlib.Path(__file__).parent.resolve()

setup(
    name="Sardine",
    version="0.0.1",
    description="Python's missing algorave module",
    author="Raphaël Forment",
    author_email="raphael.forment@gmail.com",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers, Musicians",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
    ],
    packages=find_namespace_packages(
        include=[
            "sardine",
            "fishery",
        ]
    ),
    python_requires=">=3.9, <4",
    install_requires=[
        "appdirs>=1.4",
        "mido>=1.2",
        "osc4py3>=1.0",
        "psutil>=5.0",
        "rich>=12.5",
        "lark>=1.1",
        "click>=8.1",
        "ptpython>=3.0",
        "python-rtmidi>=1.4",
        "jupyterlab>=3.4",
        "LinkPython>=0.1",
    ],
    extras_require={"speed": ["uvloop"], "dev": ["black"]},
    entry_points={
        "console_scripts": [
            "sardine-config-python    = cli.main:edit_python_configuration",
            "sardine-config-superdirt = cli.main:edit_superdirt_configuration",
            "sardine-config           = cli.main:main",
        ]
    },
)
