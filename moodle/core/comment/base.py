from moodle import BaseMoodle
from . import Comments


class BaseComment(BaseMoodle):
    def add_comments(self):
        data = self.moodle.get('core_comment_add_comments')
        return data

    def delete_comments(self):
        data = self.moodle.get('core_comment_delete_comments')
        return data

    def get_comments(self,
                     contextlevel: str,
                     instanceid: int,
                     component: int,
                     itemid: int,
                     area: str = "",
                     page: int = 0,
                     sortdirection: str = "DESC") -> Comments:
        """Returns comments.

        Args:
            contextlevel (str): contextlevel system, course, user...
            instanceid (int): the Instance id of item associated with the context level
            component (int): component
            itemid (int): associated id
            area (str, optional): string comment area. Defaults to "".
            page (int, optional): page number (0 based). Defaults to 0.
            sortdirection (str, optional): Sort direction: ASC or DESC. Defaults to "DESC".

        Returns:
            Comments: Response
        """
        data = self.moodle.get(
            'core_comment_get_comments',
            contextlevel=contextlevel,
            instanceid=instanceid,
            component=component,
            itemid=itemid,
            area=area,
            page=page,
            sortdirection=sortdirection,
        )
        return self._tr(Comments, data)
