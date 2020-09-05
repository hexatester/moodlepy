from dacite import from_dict
from typing import Optional
from moodle import BaseMoodle
from . import BadgeResponse


class BaseBadges(BaseMoodle):
    def get_user_badges(self,
                        userid: Optional[int] = 0,
                        courseid: Optional[int] = 0,
                        page: Optional[int] = 0,
                        perpage: Optional[int] = 0,
                        search: Optional[str] = None,
                        onlypublic: Optional[int] = None) -> BadgeResponse:
        """Get list of badges awarded to a user.

        Args:
            userid (Optional[int], optional): Badges only for this user id, empty for current user. Defaults to 0.
            courseid (Optional[int], optional): Filter badges by course id, empty all the courses. Defaults to 0.
            page (Optional[int], optional): The page of records to return.. Defaults to 0.
            perpage (Optional[int], optional): The number of records to return per page. Defaults to 0.
            search (Optional[str], optional): A simple string to search for. Defaults to None.
            onlypublic (Optional[int], optional): Whether to return only public badges. Defaults to None.

        Returns:
            BadgeResponse: Returns the list of badges awarded to a user
        """
        res = self.moodle.post(
            'core_badges_get_user_badges',
            userid=userid,
            courseid=courseid,
            page=page,
            perpage=perpage,
            search=search,
            onlypublic=onlypublic,
        )
        return from_dict(BadgeResponse, res)
