from setuptools import setup, find_packages #setuptools is a library that handles packaging;

setup(
    name="ft_package",             # package name metadata displayed when someone does pip show ft_package.
    version="0.0.1",               # package version
    author="okapshai",
    author_email="okapshai@42.fr",
    description="A sample test package",
    url="https://github.com/okapshai/ft_package",  # optional
    packages=find_packages(),      # finds all packages (your folder)
    python_requires=">=3.6",       # required Python version
    license="MIT"
)
