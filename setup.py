from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["ipython>=6", "nbformat>=4", "nbconvert>=5", "requests>=2"]

setup(
    name="fastplots",
    version="alpha-0.1",
    author="Jhossua Giraldo",
    author_email="jhossua.giraldo@udea.edu.co",
    description="Una librería para hacer gráficos de matplotlib rápidamente",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/Jhosscryte/fastplots/",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.7.11",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
