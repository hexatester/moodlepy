from datetime import datetime
from typing import List, Optional, Union
from moodle import BaseMoodle
from moodle.utils.helper import from_dict
from . import Discussions, Forum, NewPost


class BaseForum(BaseMoodle):
    def add_discussion(
            self,
            forumid: int,
            subject: str,
            message: str,
            groupid: int = 0,
            options: Optional[List[Discussions.Option]] = None
    ) -> Discussions.New:
        """Add a new discussion into an existing forum.

        Args:
            forumid (int): Forum instance ID
            subject (str): New Discussion subject
            message (str): New Discussion message (only html format allowed)
            groupid (int, optional): The group, default to 0. Defaults to 0.
            options (List[Discussions.Option], optional): Options. Defaults to None.

        Returns:
            Discussions.New: [description]
        """
        res = self.moodle.post(
            'mod_forum_add_discussion',
            forumid=forumid,
            subject=subject,
            message=message,
            groupid=groupid,
            options=options or [],
        )
        return from_dict(Discussions.New, res)

    def add_discussion_post(self,
                            postid: int,
                            subject: str,
                            message: str,
                            options: Optional[List[NewPost.Option]] = None,
                            messageformat: int = 1) -> NewPost:
        """Create new posts into an existing discussion.

        Args:
            postid (int): the post id we are going to reply to (can be the initial discussion post
            subject (str): new post subject
            message (str): new post message (html assumed if messageformat is not provided)
            options (List[NewPost.Option], optional): Options. Defaults to None.
            messageformat (int, optional): message format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN). Defaults to 1.

        Returns:
            NewPost: [description]
        """
        res = self.moodle.post(
            'mod_forum_add_discussion_post',
            postid=postid,
            subject=subject,
            message=message,
            options=options or [],
            messageformat=messageformat,
        )
        return from_dict(NewPost, res)

    def can_add_discussion(self, forumid: int, groupid: Optional[int] = None):
        res = self.moodle.post('mod_forum_can_add_discussion')
        return res

    def get_discussion_posts(self,
                             discussionid: int,
                             sortby: str,
                             sortdirection: str = 'DESC'):
        res = self.moodle.post('mod_forum_get_discussion_posts')
        return res

    def get_forum_access_information(self, forumid: int):
        res = self.moodle.post('mod_forum_get_forum_access_information')
        return res

    def get_forum_discussion_posts(self,
                                   discussionid: int,
                                   sortby: str = 'created',
                                   sortdirection: str = 'DESC'):
        res = self.moodle.post('mod_forum_get_forum_discussion_posts')
        return res

    def get_forum_discussions(self,
                              forumid: int,
                              sortorder: int = -1,
                              page: int = -1,
                              perpage: int = 0,
                              groupid: int = 0) -> Discussions:
        """Returns a list of forum discussions optionally sorted and paginated.

        Args:
            forumid (int): forum instance id
            sortorder (int, optional): sort by this element: numreplies, , created or timemodified. Defaults to -1.
            page (int, optional): current page. Defaults to -1.
            perpage (int, optional): items per page. Defaults to 0.
            groupid (int, optional): group id. Defaults to 0.

        Returns:
            Discussions: List of Discussion
        """
        res = self.moodle.post(
            'mod_forum_get_forum_discussions',
            forumid=forumid,
            sortorder=sortorder,
            page=page,
            perpage=perpage,
            groupid=groupid,
        )
        return from_dict(Discussions, res)

    def get_forum_discussions_paginated(self,
                                        forumid: int,
                                        sortby: str = 'timemodified',
                                        sortdirection: str = 'DESC',
                                        page: int = -1,
                                        perpage: int = 0) -> Discussions:
        """** DEPRECATED ** Please do not call this function any more. Returns a list of forum discussions optionally sorted and paginated.

        Args:
            forumid (int): forum instance id
            sortby (str, optional): sort by this element: id, timemodified, timestart or timeend. Defaults to 'timemodified'.
            sortdirection (str, optional): sort direction: ASC or DESC. Defaults to 'DESC'.
            page (int, optional): current page. Defaults to -1.
            perpage (int, optional): items per page. Defaults to 0.

        Returns:
            Discussions: list of Discussion
        """
        res = self.moodle.post(
            'mod_forum_get_forum_discussions_paginated',
            forumid=forumid,
            sortby=sortby,
            sortdirection=sortdirection,
            page=page,
            perpage=perpage,
        )
        return from_dict(Discussions, res)

    def get_forums_by_courses(self,
                              courseids: Optional[List[int]] = None
                              ) -> List[Forum]:
        """Returns a list of forum instances in a provided set of courses, if no courses are provided then all the forum instances the user has access to will be returned.

        Args:
            courseids (Optional[List[int]], optional): Array of Course IDs. Defaults to None.

        Returns:
            List[Forum]: list of Forum
        """
        datas = self.moodle.post('mod_forum_get_forums_by_courses',
                                 courseids=courseids or [])
        return [Forum.from_data(data, self.moodle)
                for data in datas] if datas else []

    def set_lock_state(self, forumid: int, discussionid: int,
                       targetstate: Union[datetime, int]):
        res = self.moodle.post('mod_forum_set_lock_state')
        return res

    def set_pin_state(self, discussionid: int, targetstate: int):
        res = self.moodle.post('mod_forum_set_pin_state')
        return res

    def set_subscription_state(self, forumid: int, discussionid: int,
                               targetstate: int):
        res = self.moodle.post('mod_forum_set_subscription_state')
        return res

    def toggle_favourite_state(self, discussionid: int, targetstate: int):
        res = self.moodle.post('mod_forum_toggle_favourite_state')
        return res

    def view_forum(self, forumid: int):
        res = self.moodle.post('mod_forum_view_forum')
        return res

    def view_forum_discussion(self, discussionid: int):
        res = self.moodle.post('mod_forum_view_forum_discussion')
        return res
