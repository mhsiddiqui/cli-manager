from setuptools import find_packages, setup

setup(
    name="cli-manager",
    version="0.1.0",
    description="""
    A package to write management commands for FastAPI,
    Flask and other similar frameworks using Python Click.
    Inspired by Django management commands
    """,
    author="Muhammad Hassan Siddiqui",
    author_email="mhassan.eeng@gmail.com",
    packages=find_packages(exclude=["tests*", "example*"]),
    install_requires=["click>=8.0", "pytest>=7.0", "httpx>=0.23", "pytest-click>=1.0"],
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
