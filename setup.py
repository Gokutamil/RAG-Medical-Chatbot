from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="Medical RAG",
    version="0.1",
    author="Gokul",
    packages=find_packages(),
    install_requires = requirements,
)