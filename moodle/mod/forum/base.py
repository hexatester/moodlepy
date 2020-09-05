from typing import Iterable
from moodle import BaseMoodle
from moodle.utils.helper import from_dict
from . import Forum


class BaseForum(BaseMoodle):
    def get_forums_by_courses(self) -> Iterable[Forum]:
        datas = self.moodle.get('mod_forum_get_forums_by_courses')
        if datas:
            return [from_dict(Forum, data) for data in datas]
        return []
