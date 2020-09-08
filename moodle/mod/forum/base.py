from typing import List, Optional
from moodle import BaseMoodle
from . import Forum


class BaseForum(BaseMoodle):
    def get_forums_by_courses(self,
                              courseids: Optional[List[int]] = None
                              ) -> List[Forum]:
        datas = self.moodle.get('mod_forum_get_forums_by_courses',
                                courseids=courseids or [])
        return [Forum.from_data(data, self.moodle)
                for data in datas] if datas else []
