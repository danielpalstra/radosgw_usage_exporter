#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open("README.md") as readme_file:
    readme = readme_file.read()

requirements = [
    "prometheus-client==0.0.19",
    "requests>=2.20.0",
    "boto==2.46.1",
    "requests-aws==0.1.8",
]

setup_requirements = ["setuptools_scm"]

test_requirements = []

setup(
    author="blemmenes",
    python_requires=">=3.5",
    classifiers=[
        "Development Status :: 2 - Beta",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="Prometheus exporter for scraping Ceph RADOSGW usage data.",
    install_requires=requirements,
    long_description=readme,
    include_package_data=True,
    keywords="radosgw_usage_exporter",
    name="radosgw_usage_exporter",
    packages=find_packages(
        include=["radosgw_usage_exporter", "radosgw_usage_exporter.*"]
    ),
    entry_points={
        "console_scripts": [
            "radosgw_usage_exporter=radosgw_usage_exporter.radosgw_usage_exporter:main"
        ],
    },
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/blemmenes/radosgw_usage_exporter",
    version="2020.7.0",
    zip_safe=False,
)
