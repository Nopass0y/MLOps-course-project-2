from setuptools import setup, find_packages

with open("requirements.txt", "r") as fh:
    requirements = fh.read().splitlines()

setup(
    name="DEVOPS-PROJECT-2",
    version="0.0.1",
    author="Yossapon",
    packages= find_packages(),
    install_requires=requirements,
)