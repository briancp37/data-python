## data-python
Data aggregator for Exchanges

## Motivation
To personally host cryptocurrency price data, network data, etc. in the cloud for use in trading projects.

## Build status
Early beta mode.  Data download is stable from BigQuery.

[![Build Status](https://travis-ci.org/akashnimare/foco.svg?branch=master)](https://travis-ci.org/akashnimare/foco)
[![Windows Build Status](https://ci.appveyor.com/api/projects/status/github/akashnimare/foco?branch=master&svg=true)](https://ci.appveyor.com/project/akashnimare/foco/branch/master)

## Code style
Project is pep8 compliant.

[![PEP8](https://img.shields.io/badge/code%20style-pep8-orange.svg)](https://www.python.org/dev/peps/pep-0008/)
 
## Screenshots
Include logo/demo screenshot etc.

## Tech/framework used
Ex. -

<b>Built with</b>
- [Electron](https://electron.atom.io)
- [Google BigQuery](https://cloud.google.com/bigquery/docs/)
- [Google Sheets](https://developers.google.com/apps-script/reference/spreadsheet)
- [Python Pandas](https://pandas.pydata.org/pandas-docs/stable/)
<!-- and without jargon in this [Technograph article](http://www.dailyillini.com/article/2016/04/automatic-speech-recognition). -->
<!-- ## Features
What makes your project stand out?

## Code Example
Show what the library does as concisely as possible, developers should be able to figure out **how** your project solves their problem by looking at the code example. Make sure the API you are showing off is obvious, and that your code is short and concise.

## Installation
Provide step by step series of examples and explanations about how to get a development env running.

## Tests
Describe and show how to run the tests with code examples.

## How to use?
If people like your project they’ll want to learn how they can use it. To do so include step by step guide to use your project.
-->
## File Structure
```
|__ .vscode
    |__ settings.json
|__ kraken
    |__ __init__.py
    |__ api.py
    |__ BigQuery.py
    |__ helpers.py
    |__ test.py
|__ __init_.py
|__ README.md
|__ requirements_dev.txt
|__ setup.py
```

## Useful Links
- [Package setup instructions](https://towardsdatascience.com/build-your-first-open-source-python-project-53471c9942a7)
- [README instructions](https://medium.com/@meakaakka/a-beginners-guide-to-writing-a-kickass-readme-7ac01da88ab3)
- [Github commits](https://medium.com/@panjeh/makefile-git-add-commit-push-github-all-in-one-command-9dcf76220f48)