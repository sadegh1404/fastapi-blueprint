from setuptools import setup, find_packages

setup(
    name="fastapi_blueprint",
    version="1.0.0",
    description="A CLI tool to generate file structure for FastAPI projects.",
    author="Sadegh Ranjbar",
    author_email="sadegh.r1404@gmail.com",
    packages=find_packages(),
    long_description=open("README.md").read(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "fastapi-blueprint=fastapi_blueprint.cli:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.6",
)
