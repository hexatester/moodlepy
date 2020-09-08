from pytest import fixture
from typing import List

from moodle import Moodle
from moodle.core.course import Course


@fixture
def moodle() -> Moodle:
    domain = 'https://school.moodledemo.net'
    username = 'manager'
    password = 'moodle'
    return Moodle.login(domain, username, password)


@fixture
def user_id(moodle: Moodle) -> int:
    site_info = moodle.core.webservice.get_site_info()
    return site_info.userid


@fixture
def courses(moodle: Moodle) -> List[Course]:
    return moodle.core.course.get_courses()
