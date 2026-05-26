from setuptools import setup, find_packages

setup(
    name="password-generator",
    version="1.0.0",
    author="Francesco Castaldi",
    description="A simple cross-platform UI password generator",
    packages=find_packages(),
    python_requires=">=3.9",
    install_requires=[
        "pyperclip>=1.8.2",
    ],
)
