from typing import List

from moodle import BaseMoodle
from moodle.base.general import GeneralStatus
from .page import PagesResponse


class BasePage(BaseMoodle):
    def get_pages_by_courses(self, courseids: List[int]) -> PagesResponse:
        """Returns a list of pages in a provided list of courses, if no list is provided all pages that the user can view will be returned.

        Args:
            courseids (List[int]): Array of course ids

        Returns:
            PagesResponse: Response
        """
        data = self.moodle.post(
            'mod_page_get_pages_by_courses',
            courseids=courseids,
        )
        return self._tr(PagesResponse, **data)

    def view_page(self, pageid: int) -> GeneralStatus:
        """Simulate the view.php web interface page: trigger events, completion, etc...

        Args:
            pageid (int): page instance id

        Returns:
            GeneralStatus: Response
        """
        data = self.moodle.post(
            'mod_page_view_page',
            pageid=pageid,
        )
        return self._tr(GeneralStatus, **data)
