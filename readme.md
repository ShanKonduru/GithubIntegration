# GitHub Integration

[![Python Version](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/release/python-311/)
[![PyGithub Version](https://img.shields.io/badge/PyGithub-1.59.1-blue.svg)](https://github.com/PyGithub/PyGithub)
[![python-dateutil Version](https://img.shields.io/badge/python--dateutil-2.8.2-blue.svg)](https://github.com/dateutil/dateutil)

## Description

Python code to integrate and read GitHub APIs.

## Installation

You can install the required dependencies using [Poetry](https://python-poetry.org/):

```python
poetry install
```

## Dependencies
Python (>=3.11)
PyGithub (>=1.59.1)
python-dateutil (>=2.8.2)

## Scripts

### getallcommits.py
Description: Script to retrieve all commits from a GitHub repository.

### getcommitsbetweendates.py
Description: Script to retrieve commits between specified dates from a GitHub repository.

### getcommitsforafile.py
Description: Script to retrieve commits for a specific file within a date range from a GitHub repository.

### getfiles.py
Description: Script to retrieve the list of files changed in a commit from a GitHub repository.

### getrepos.py
Description: Script to retrieve the list of repositories for a GitHub user or organization.

## Execution of Python scripts

### Setup
Change the following properties before running the script
```python
ACCESS_TOKEN="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"
REPO_OWNER = "ShanKonduru"
REPO_NAME = "PostmanCollectionTestcaseExtractor"
```

### USAGE
In the visual studio code terminal or command window, use the following commands to run each python script file

```python
python .\getallcommits.py
python .\getcommitsbetweendates.py
python .\getcommitsforafile.py
python .\getfiles.py
python .\getrepos.py
```

### License
This project is licensed under the MIT License.

### Authors
ShanKonduru ShanKonduru@gmail.com
