from typing import Optional
from moodle import BaseMoodle
from . import Blocks


class BaseBlock(BaseMoodle):
    def get_course_blocks(self,
                          courseid: int,
                          returncontents: Optional[int] = None) -> Blocks:
        """Blocks information for a course.

        Args:
            courseid (int): course id
            returncontents (Optional[int], optional): Whether to return the block contents.. Defaults to None.

        Returns:
            Blocks: Returns blocks information for a course.
        """
        res = self.moodle.post('core_block_get_course_blocks',
                               courseid=courseid,
                               returncontents=returncontents)
        return self._tr(Blocks, **res)

    def get_dashboard_blocks(self,
                             userid: int = 0,
                             returncontents: bool = True) -> Blocks:
        """blocks information for the given user dashboard.

        Args:
            userid (int, optional): User id, default is current user. Defaults to 0.
            returncontents (bool, optional): Whether to return the block contents. Defaults to True.

        Returns:
            Blocks: Returns blocks information for the given user dashboard.
        """
        res = self.moodle.post('core_block_get_dashboard_blocks',
                               userid=userid,
                               returncontents=1 if returncontents else 0)
        return self._tr(Blocks, **res)
