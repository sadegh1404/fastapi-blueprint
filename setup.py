from setuptools import setup, find_packages

setup(
    name="fastapi-cli",
    version="1.0.0",
    description="A CLI tool to generate file structure for FastAPI projects.",
    author="Sadegh Ranjbar",
    author_email="sadegh.r1404@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    entry_points={
        "console_scripts": [
            "fastapi-cli=fastapi_cli:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.6",
)
