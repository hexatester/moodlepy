from typing import List

from moodle import BaseMoodle
from . import RecentlyAccessedItem, StarredCourse


class Block(BaseMoodle):
    def recentlyaccesseditems_get_recent_items(self,
                                               limit: int = 0
                                               ) -> List[RecentlyAccessedItem]:
        """List of items a user has accessed most recently.

        Args:
            limit (int, optional): result set limit. Defaults to 0.

        Returns:
            List[RecentlyAccessedItem]: The most recently accessed activities/resources by the logged user
        """
        data = self.moodle.post(
            'block_recentlyaccesseditems_get_recent_items',
            limit=limit,
        )
        return self._trs(RecentlyAccessedItem, data)

    def starredcourses_get_starred_courses(self,
                                           limit: int = 0,
                                           offset: int = 0
                                           ) -> List[StarredCourse]:
        """Get users starred courses.

        Args:
            limit (int, optional): Limit. Defaults to 0.
            offset (int, optional): Offset. Defaults to 0.

        Returns:
            List[StarredCourse]: users starred courses
        """
        data = self.moodle.post(
            'block_starredcourses_get_starred_courses',
            limit=limit,
            offset=offset,
        )
        return self._trs(StarredCourse, data)
