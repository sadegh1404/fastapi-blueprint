from setuptools import setup, find_packages

setup(
    name="fastapi_blueprint",
    version="1.0.2",
    description="A CLI tool to generate file structure for FastAPI projects.",
    author="Sadegh Ranjbar",
    author_email="sadegh.r1404@gmail.com",
    packages=find_packages(),
    long_description=open("README.rst", encoding="utf-8").read(),
    long_description_content_type="text/x-rst",
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
