from typing import List

from moodle import BaseMoodle
from . import Urls, View


class BaseUrl(BaseMoodle):
    def get_urls_by_courses(self, courseids: List[int]) -> Urls:
        """Returns a list of urls in a provided list of courses, if no list is provided all urls that the user can view will be returned.

        Args:
            courseids (List[int]): Array of course ids

        Returns:
            Urls: List of Url
        """
        res = self.moodle.post(
            'mod_url_get_urls_by_courses',
            courseids=courseids,
        )
        return Urls(**res)  # type: ignore

    def view_url(self, urlid: int) -> View:
        """Trigger the course module viewed event and update the module completion status.

        Args:
            urlid (int): url instance id

        Returns:
            View: Response
        """
        res = self.moodle.post('mod_url_view_url', urlid=urlid)
        return View(**res)  # type: ignore
