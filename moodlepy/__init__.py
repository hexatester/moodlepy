from .base.moodle_object import MoodleObject
from .base.base_moodle import BaseMoodle

from .mod.forum.forum import Forum

from .mod.mod import Mod
from .moodle import Moodle

from .version import __version__  # NOQA

__all__ = ['BaseMoodle', 'Forum', 'Mod', 'Moodle', 'MoodleObject']
