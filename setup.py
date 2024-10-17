from setuptools import setup, find_packages

setup(
    name="fastapi-commands",
    version="0.1.0",
    description="Management command system for FastAPI",
    author="Your Name",
    author_email="youremail@example.com",
    packages=find_packages(exclude=["tests*"]),
    install_requires=[
        "click>=8.0",
        "pytest>=7.0",
        "httpx>=0.23",
        "pytest-click>=1.0"
    ],
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
