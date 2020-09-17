from moodle import (
    __version__,
    Auth,
    Core,
    Mod,
    Tool,
    Moodle,
)


def test_version():
    assert __version__ == '0.8.1'


def test_moodle(moodle: Moodle):
    assert isinstance(moodle, Moodle)
    assert isinstance(moodle.auth, Auth)
    assert isinstance(moodle.core, Core)
    assert isinstance(moodle.mod, Mod)
    assert isinstance(moodle.tool, Tool)
