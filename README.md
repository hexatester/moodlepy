# moodlepy

[![moodlepy - PyPi](https://img.shields.io/pypi/v/moodlepy)](https://pypi.org/project/moodlepy/)
[![codecov](https://codecov.io/gh/hexatester/moodlepy/branch/master/graph/badge.svg)](https://codecov.io/gh/hexatester/moodlepy)
[![BUILD](https://img.shields.io/travis/com/hexatester/moodlepy)](https://travis-ci.com/github/hexatester/moodlepy)
[![LICENSE](https://img.shields.io/github/license/hexatester/moodlepy)](https://github.com/hexatester/moodlepy/blob/master/LICENSE)

Python client for moodle webservice

## Introduction

This library provide a pure Python interface for [Moodle Web Service](https://docs.moodle.org/dev/Web_services). It's compatible with Python versions 3.6+

## Moodle Web Service support

Not all types and methods are supported, since moodlepy is not yet released.

## Installing

You can install or upgrade moodlepy with:

```bash
pip install moodlepy --upgrade
```

Or you can install from source with:

```bash
git clone https://github.com/hexatester/moodlepy
cd moodlepy
python setup.py install
```

## Usage

Example usage

```python
from moodle import Moodle
url = 'https://my.domain/webservice/rest/server.php'
token = 'super secret token'
moodle = Moodle(url, token)
raw_site_info = moodle('core_webservice_get_site_info')
site_info = moodle.core.webservice.get_site_info()  # return typed site_info

print(raw_site_info)
print(site_info)
```

In the future all [Web service functions](https://docs.moodle.org/dev/Web_service_API_functions) will covered by moodlepy
