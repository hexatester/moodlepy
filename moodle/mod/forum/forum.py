from __future__ import annotations
from dataclasses import dataclass
from typing import List, Type, TYPE_CHECKING
from moodle import MoodleObject
if TYPE_CHECKING:
    from moodle import Moodle


@dataclass
class Forum(MoodleObject):
    id: int
    course: int
    type: str
    name: str
    intro: str
    introformat: int
    introfiles: list
    duedate: int
    cutoffdate: int
    assessed: int
    assesstimestart: int
    assesstimefinish: int
    scale: int
    maxbytes: int
    maxattachments: int
    forcesubscribe: int
    trackingtype: int
    rsstype: int
    rssarticles: int
    timemodified: int
    warnafter: int
    blockafter: int
    blockperiod: int
    completiondiscussions: int
    completionreplies: int
    completionposts: int
    cmid: int
    numdiscussions: int
    cancreatediscussions: bool
    lockdiscussionafter: int
    istracked: bool

    @classmethod
    def inject(cls, moodle: Moodle) -> Type[Forum]:
        cls.moodle = moodle
        return cls

    @classmethod
    def get_forums_by_courses(cls) -> List[Forum]:
        datas = cls.moodle.get('mod_forum_get_forums_by_courses')
        if datas:
            return [cls(**data) for data in datas]
        return []
