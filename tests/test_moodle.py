from moodle import (
    __version__,
    Auth,
    Core,
    Enrol,
    Mod,
    Tool,
    Moodle,
)


def test_version():
    assert __version__ == '0.22.0'


def test_moodle(moodle: Moodle):
    assert isinstance(moodle, Moodle)
    assert isinstance(moodle.auth, Auth)
    assert isinstance(moodle.core, Core)
    assert isinstance(moodle.enrol, Enrol)
    assert isinstance(moodle.mod, Mod)
    assert isinstance(moodle.tool, Tool)
