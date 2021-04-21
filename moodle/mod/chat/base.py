from datetime import datetime
from typing import List, Union

from moodle import BaseMoodle


class BaseChat(BaseMoodle):
    def get_chat_latest_messages(
        self, chatsid: str, chatlasttime: Union[int, datetime] = 0
    ):
        data = self.moodle.post(
            "mod_chat_get_chat_latest_messages",
            chatsid=chatsid,
            chatlasttime=chatlasttime,
        )
        return data

    def get_chat_users(self, chatsid: str):
        data = self.moodle.post(
            "mod_chat_get_chat_users",
            chatsid=chatsid,
        )
        return data

    def get_chats_by_courses(self, courseids: List[int]):
        data = self.moodle.post(
            "mod_chat_get_chats_by_courses",
            courseids=courseids,
        )
        return data

    def get_session_messages(
        self,
        chatid: int,
        sessionstart: Union[int, datetime],
        sessionend: Union[int, datetime],
        groupid: int = 0,
    ):
        data = self.moodle.post(
            "mod_chat_get_session_messages",
            chatid=chatid,
            sessionstart=sessionstart,
            sessionend=sessionend,
            groupid=groupid,
        )
        return data

    def get_sessions(self, chatid: int, groupid: int = 0, showall: int = None):
        data = self.moodle.post(
            "mod_chat_get_sessions",
            chatid=chatid,
            groupid=groupid,
            showall=showall or "",
        )
        return data

    def login_user(self, chatid: int, groupid: int = 0):
        data = self.moodle.post(
            "mod_chat_login_user",
            chatid=chatid,
            groupid=groupid,
        )
        return data

    def send_chat_message(self, chatsid: str, messagetext: str, beepid: str = ""):
        data = self.moodle.post(
            "mod_chat_send_chat_message",
            chatsid=chatsid,
            messagetext=messagetext,
            beepid=beepid,
        )
        return data

    def view_chat(self, chatid: int):
        data = self.moodle.post(
            "mod_chat_view_chat",
            chatid=chatid,
        )
        return data
