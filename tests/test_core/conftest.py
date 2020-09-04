from pytest import fixture
from moodle import Moodle


@fixture
def moodle() -> Moodle:
    domain = 'https://school.moodledemo.net'
    username = 'manager'
    password = 'moodle'
    return Moodle.login(domain, username, password)
