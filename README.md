# moodlepy

[![moodlepy - PyPi](https://img.shields.io/pypi/v/moodlepy)](https://pypi.org/project/moodlepy/)
[![codecov](https://codecov.io/gh/hexatester/moodlepy/branch/master/graph/badge.svg)](https://codecov.io/gh/hexatester/moodlepy)
[![BUILD](https://img.shields.io/travis/com/hexatester/moodlepy)](https://travis-ci.com/github/hexatester/moodlepy)
[![LICENSE](https://img.shields.io/github/license/hexatester/moodlepy)](https://github.com/hexatester/moodlepy/blob/master/LICENSE)

Python client for moodle webservice

## Introduction

This library provide a pure Python interface for [Moodle Web Service](https://docs.moodle.org/dev/Web_services). It's compatible with Python versions 3.7+

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

# or
from moodle import Mdl
from moodle.core.webservice import BaseWebservice

moodle = Mdl(url, token)
webservice = BaseWebservice(moodle)
site_info2 = webservice.get_site_info()

assert site_info == site_info2
```

In the future all [Web service functions](https://docs.moodle.org/dev/Web_service_API_functions) will be covered by moodlepy

# Moodle Web Service support

❗️ Not all types and methods are supported, since moodlepy is not yet released.
A = Added, W = Work In Progress

| Area                 | Functions | Types | Tests | Status |
| -------------------- | --------- | ----- | ----- | ------ |
| auth_email           | A         | A     |       |        |
| block                |           |       |       |        |
| core_auth            | A         | A     |       |        |
| core_backup          |           |       |       |        |
| core_badge           | A         | A     | A     |        |
| core_blog            | A         | A     | A     |        |
| core_calendar        | A         | A     |       | W      |
| core_cohort          |           |       |       |        |
| core_comment         |           |       |       | W      |
| core_competency      |           |       |       |        |
| core_completion      | A         | A     |       |        |
| core_course          |           |       |       | W      |
| core_customfield     |           |       |       |        |
| core_enrol           |           |       |       |        |
| core_fetch           |           |       |       | W      |
| core_files           |           |       |       | W      |
| core_filters         |           |       |       |        |
| core_form            |           |       |       | W      |
| core_get             |           |       |       | W      |
| core_grade           |           |       |       | W      |
| core_grades          |           |       |       |        |
| core_grading         |           |       |       |        |
| core_group           |           |       |       |        |
| core_h5p             |           |       |       |        |
| core_message         | A         |       |       | W      |
| core_notes           | A         | A     |       | W      |
| core_output          |           |       |       |        |
| core_question        | W         |       |       | W      |
| core_rating          |           |       |       |        |
| core_role            |           |       |       |        |
| core_search          |           |       |       | W      |
| core_session         |           |       |       | W      |
| core_tag             |           |       |       |        |
| core_update          |           |       |       |        |
| core_user            |           |       |       | W      |
| core_webservice      | A         | A     | A     | A      |
| enrol_guest          |           |       |       |        |
| enrol_manual         |           |       |       |        |
| enrol_self           |           |       |       |        |
| gradereport_overview |           |       |       |        |
| gradereport_user     |           |       |       |        |
| gradingform_guide    |           |       |       |        |
| gradingform_rubric   |           |       |       |        |
| local_mobile         |           |       |       | W      |
| message_airnotifier  |           |       |       | W      |
| message_popup        |           |       |       | W      |
| mod_assign           |           |       |       | W      |
| mod_book             |           |       |       |        |
| mod_chat             |           |       |       | W      |
| mod_choice           |           |       |       |        |
| mod_data             |           |       |       |        |
| mod_feedback         |           |       |       |        |
| mod_folder           | A         | A     |       |        |
| mod_forum            |           |       |       | W      |
| mod_glossary         |           |       |       |        |
| mod_imscp            |           |       |       |        |
| mod_label            |           |       |       |        |
| mod_lesson           |           |       |       | W      |
| mod_lti              |           |       |       |        |
| mod_page             |           |       |       | W      |
| mod_quiz             |           |       |       | W      |
| mod_resource         | A         | A     |       |        |
| mod_scorm            |           |       |       |        |
| mod_survey           |           |       |       | W      |
| mod_url              | A         | A     |       |        |
| mod_wiki             |           |       |       |        |
| mod_workshop         |           |       |       |        |
| report_competency    |           |       |       |        |
| report_insights      |           |       |       |        |
| tool_analytics       |           |       |       |        |
| tool_lp              |           |       |       |        |
| tool_mobile          | A         | A     |       | W      |
| tool_templatelibrary |           |       |       |        |
| tool_usertours       |           |       |       |        |
| tool_xmldb           |           |       |       |        |
