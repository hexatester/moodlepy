from typing import List, Optional
from moodle import BaseMoodle
from . import BlogEntries, ViewEntry

Filter = BlogEntries.Filter


class BaseBlog(BaseMoodle):
    def get_entries(
        self, filters: Optional[List[Filter]] = None, page: int = 0, perpage: int = 10
    ) -> BlogEntries:
        """Get blog entries.

        Args:
            filters (Optional[List[Filter]], optional): Parameters to filter blog listings. Defaults to None.
            page (int, optional): The blog page to return. Defaults to 0.
            perpage (int, optional): The number of posts to return per page. Defaults to 10.

        Returns:
            BlogEntries: Returns blog entries.
        """
        res = self.moodle.post(
            "core_blog_get_entries", filters=filters or [], page=page, perpage=perpage
        )
        return self._tr(BlogEntries, **res)

    def view_entries(self, filters: Optional[List[Filter]] = None) -> ViewEntry:
        """Trigger the blog_entries_viewed event.

        Args:
            filters (Optional[List[Filter]], optional): Parameters used in the filter of view_entries.. Defaults to None.

        Returns:
            ViewEntry: the blog_entries_viewed response.
        """
        res = self.moodle.post("core_blog_view_entries", filters=filters)
        return self._tr(ViewEntry, **res)
