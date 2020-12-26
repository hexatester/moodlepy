# How To Contribute

Every open source project lives from the generous help by contributors that sacrifice their time and moodlepy is no different. To make participation as pleasant as possible, this project adheres to the [Code of Conduct](https://www.contributor-covenant.org/version/1/4/code-of-conduct/) by contributor-covenant.

## Setting things up

### Setup

1. Fork the moodlepy repository to your GitHub account.

2. Clone your forked repository of moodlepy to your computer:

```bash
$ git clone https://github.com/<your username>/moodlepy
$ cd moodlepy
```

3. Add a track to the original repository:

```bash
$ git remote add upstream https://github.com/moodlepy/moodlepy
```

4. Install dependencies with [poetry](https://python-poetry.org/):

```bash
$ pip install poetry
$ poetry install --no-root
```

5. Install pre-commit hooks:

```bash
$ pre-commit install
```

### IDE

Recommended linter (linting) `mypy` and code formater `yapf`.

## Finding something to do

If you already know what you'd like to work on, you can skip this section.

If you have an idea for something to do, first check if it's already been filed on the [issue tracker](https://github.com/hexatester/moodlepy/issues). If so, add a comment to the issue saying you'd like to work on it, and we'll help you get started! Otherwise, please file a new issue and assign yourself to it.

Another great way to start contributing is by writing tests. Tests are really important because they help prevent developers from accidentally breaking existing code, allowing them to build cool things faster.

That being said, we want to mention that we are very hesitant about adding new requirements to our projects. If you intend to do this, please state this in an issue and get a verification from the maintainer.

## Implementing function

Currently we are using moodle sandbox as webdocumentation source.

### Login as admin

Log in to [moodle sandbox](https://sandbox.moodledemo.net/) with username `admin` password `sandbox`.

### Enabling Web Services

1. Open Site admiistration > Plugins > Web Services > Overview
2. [Enable web services](https://sandbox.moodledemo.net/admin/search.php?query=enablewebservices). Check the checkbox and Save changes.

### Open API Documentation for webservice

Open Site admiistration > Plugins > Web Services > API Documentation ([API Documentation](https://sandbox.moodledemo.net/admin/webservice/documentation.php))
