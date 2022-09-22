from gettext import find
import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name = "diffco",
    version="0.1",
    description="Automatic differentiation of R^n metric spaces",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Fatlonder/diffco",
    packages=setuptools.find_packages()
)