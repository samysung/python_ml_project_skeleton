# python ml skeleton project
generic skeleton for machine learning project with python, hydra, pytest, sphinx, github actions, etc.
with dummy functionalities!
It is mostly oriented geospatial projects

[![PyPI python](https://img.shields.io/pypi/pyversions/pmps)](https://pypi.org/project/pmps)
[![PyPI version](https://badge.fury.io/py/pmps.svg)](https://pypi.org/project/pmps)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENCE)
[![Documentation Status](https://readthedocs.org/projects/kornia/badge/?version=latest)](https://python-ml-project-skeleton.readthedocs.io/en/latest)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/samysung/python_ml_project_skeleton/main.svg)](https://results.pre-commit.ci/latest/github/samysung/python_ml_project_skeleton/main)
[![codecov](https://codecov.io/gh/samysung/python_ml_project_skeleton/branch/main/graph/badge.svg?token=AP5UNFJXCU)](https://codecov.io/gh/samysung/python_ml_project_skeleton)

## Why this project?

The goal of this project is to present a standard architecture of python repository/package
including a full CiCd pipeline to document/test/deploy your project with standard methods
of 2022. It can be used as starting point for any project without reinventing the wheel.

## The code has no interest!

The code of this project is totally dummy: it makes simple
mathematics operations like addition and subtration!
The next iteration will make the opetations more interesting by
using multi-layers perceptron! It will try to add a complete example of Hydra
configuration.
<br/><br/>In a close future, it will serve as a demonstrator by the example
of a standard ML pipeline for experimentation and production

## Installation

### Install requirements
As Gdal dependencies are presents it's preferable to
install dependencis via conda before installing the package:
```bash
  git clone https://github.com/samysung/python_ml_project_skeleton
  cd python_ml_project_skeleton/packaging
  conda env create -f package_env.yml
  ```
### From pip:

  ```bash
  pip install pmps
  or pip install pmps==vx.x # for a specific version
  ```

<details>
  <summary>Other installation options</summary>

  #### From source:

  ```bash
  python setup.py install
  ```

  #### From source with symbolic links:

  ```bash
  pip install -e .
  ```

  #### From source using pip:

  ```bash
  pip install git+https://github.com/samysung/python_ml_project_skeleton
  ```

</details>

## Project Architecture


```bash


├── CHANGELOG.rst
├── .codecov.yml
├── deploy
│   └── dockerfile
├── docs
│   ├── add.rst
│   ├── build.sh
│   ├── changelog.rst
│   ├── conf.py
│   ├── deploy.sh
│   ├── index.rst
│   ├── Makefile
│   ├── readme_link.md
│   └── _static
│       └── img
├── .github
│   └── workflows
│       ├── publish.yml
│       ├── test_code.yml
│       ├── test_docs.yml
│       ├── test_packaging.yml
│       └── test_publish.yml
├── .gitignore
├── LICENSE
├── packaging
│   ├── doc_env.yml
│   ├── doc_requirements.txt
│   ├── package_env.yml
│   ├── requirements.txt
│   ├── test_env.yml
│   └── test_requirements.txt
├── pmps
│   ├── api
│   │   ├── add.py
│   │   ├── __init__.py
│   │   └── subtract.py
│   ├── core
│   │   ├── add.py
│   │   ├── __init__.py
│   │   └── subtract.py
│   └── __init__.py
├── .pre-commit-config.yaml
├── .pylintrc
├── README.md
├── readthedocs.yml
├── setup.cfg
├── setup.py
├── tests
│   ├── api
│   │   ├── __init__.py
│   │   ├── test_add.py
│   │   └── test_subtract.py
│   └── __init__.py
└── VERSION

```

### Architecture component overview

| **Component**                   | **Path**               | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|---------------------------------|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Python Package                  | pmps/                  | where the python executable code is localized. It is your root package as it's the first directory to contain a __init__.py and its name is generally the one you choose for your publishing package (the one build and published on forge like pypi conda, etc. Don't forget for any subpackage to add an __init__.py module to declare it as python package. NB: separate core and api in different sub package is a design choice not standard, it comes from java world but a lot of python project prefers declaring private python modules. |
 | Documentation                   | docs/                  | the source code of your documentation: conf.py is where you configure your sphinx doc, _static/ for your additional statis files (img, text, icon, video, etc.), doc is built under docs/_build/html but can be modified in maekfile.                                                                                                                                                                                                                                                                                                             |
 | Tests Package                   | tests/                 | where you organize the test code of your executable code. Your unit tests (pytest is the library used) should at least test what you expose to your clients, you can add static analysis of your tests code with extentions like mypy and flake8. Use the pytest-cov extension to produce test cover reporting.                                                                                                                                                                                                                                   |
 | Python Env                      | packaging/             | Place for your conda environment files and requirement files.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
 | Deployment                      | deploy/                | Place for Dockerfiles or any other deployment solution                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
 | CI/CD workflows                 | .github/               | github workflows configuration files (details below)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
 | CD (Documentation publishing)   | .readthedocs.yml       | configuration of the documentation publication on readthedocs (see [readthedocs link](https://readthedocs.org/))                                                                                                                                                                                                                                                                                                                                                                                                                                  |
 | CI (tests covering publishing)  | .codecov.yml           | configuration of the code covering pubication on codecov (see [codecov](https://about.codecov.io/))                                                                                                                                                                                                                                                                                                                                                                                                                                               |
 | CI (static analysis publishing) | .pre-commit.yml        | configuration of the pre-commit publication (see [pre-commit](https://pre-commit.ci/))                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
 | CD (packaging)                  | setup.cfg and setup.py | configuration files for packaging on pipy, local, etc (see [python doc](https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/))                                                                                                                                                                                                                                                                                                                                                                                   |


### CI/CD pipeline
The first and essential goal is to have a skeleton quickly editable for a lot of use case projects
with a big emphasis on continuous integration and continuous deployment.
Here is a schematic view of the Ci/Cd pipeline targeted for
open source python project, largely inspired by others well
known projects:

![Ci/Cd diagram](docs/_static/img/CiCd_pipeline.svg)
