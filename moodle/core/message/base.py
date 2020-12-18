from datetime import datetime
from typing import List, Optional, Union

from moodle import BaseMoodle, Warning
from moodle.utils.helper import from_dict
from . import ContactRequest


class BaseMessage(BaseMoodle):
    def block_contacts(self,
                       userids: List[int],
                       userid: int = 0) -> List[Warning]:
        """** DEPRECATED ** Please do not call this function any more. Block contacts

        Args:
            userids (List[int]): List of user IDs
            userid (int, optional): The id of the user we are blocking the contacts for, 0 for the current user. Defaults to 0.

        Returns:
            List[Warning]: list of warnings
        """
        res = self.moodle.post(
            'core_message_block_contacts',
            userids=userids,
            userid=userid,
        )
        return [from_dict(Warning, data) for data in res] if res else []

    def block_user(self, userid: int, blockeduserid: int) -> List[Warning]:
        """Blocks a user

        Args:
            userid (int): The id of the user who is blocking
            blockeduserid (int): The id of the user being blocked

        Returns:
            List[Warning]: list of warnings
        """
        res = self.moodle.post(
            'core_message_block_user',
            userid=userid,
            blockeduserid=blockeduserid,
        )
        return [from_dict(Warning, data) for data in res] if res else []

    def confirm_contact_request(self, userid: int,
                                requesteduserid: int) -> List[Warning]:
        """Confirms a contact request

        Args:
            userid (int): The id of the user making the request
            requesteduserid (int): The id of the user being requested

        Returns:
            List[Warning]: list of warnings
        """
        res = self.moodle.post(
            'core_message_confirm_contact_request',
            userid=userid,
            requesteduserid=requesteduserid,
        )
        return [from_dict(Warning, data) for data in res] if res else []

    def create_contact_request(self, userid: int,
                               requesteduserid: int) -> ContactRequest:
        """Creates a contact request

        Args:
            userid (int): The id of the user making the request
            requesteduserid (int): The id of the user being requested

        Returns:
            ContactRequest: ContactRequest object
        """
        res = self.moodle.post(
            'core_message_create_contact_request',
            userid=userid,
            requesteduserid=requesteduserid,
        )
        return from_dict(ContactRequest, res)

    def create_contacts(self,
                        userids: List[int],
                        userid: int = 0) -> List[Warning]:
        """** DEPRECATED ** Please do not call this function any more. Add contacts to the contact list

        Args:
            userids (List[int]): List of user IDs
            userid (int, optional): The id of the user we are creating the contacts for, 0 for the current user. Defaults to 0.

        Returns:
            List[Warning]: list of warnings
        """
        res = self.moodle.post(
            'core_message_create_contacts',
            userids=userids,
            userid=userid,
        )
        return [from_dict(Warning, data) for data in res] if res else []

    def data_for_messagearea_contacts(self,
                                      userid: int,
                                      limitfrom: int = 0,
                                      limitnum: int = 0):
        res = self.moodle.post(
            'core_message_data_for_messagearea_contacts',
            userid=userid,
            limitfrom=limitfrom,
            limitnum=limitnum,
        )
        return res

    def data_for_messagearea_conversations(self,
                                           userid: int,
                                           limitfrom: int = 0,
                                           limitnum: int = 0):
        res = self.moodle.post(
            'core_message_data_for_messagearea_conversations',
            userid=userid,
            limitfrom=limitfrom,
            limitnum=limitnum,
        )
        return res

    def data_for_messagearea_messages(self,
                                      currentuserid: int,
                                      otheruserid: int,
                                      limitfrom: int = 0,
                                      limitnum: int = 0,
                                      newest: Optional[int] = None,
                                      timefrom: Union[datetime, int] = 0):
        res = self.moodle.post(
            'core_message_data_for_messagearea_messages',
            currentuserid=currentuserid,
            otheruserid=otheruserid,
            limitfrom=limitfrom,
            limitnum=limitnum,
            newest=newest,
            timefrom=timefrom,
        )
        return res

    def data_for_messagearea_search_messages(self,
                                             userid: int,
                                             search: str,
                                             limitfrom: int = 0,
                                             limitnum: int = 0):
        res = self.moodle.post(
            'core_message_data_for_messagearea_search_messages',
            userid=userid,
            search=search,
            limitfrom=limitfrom,
            limitnum=limitnum,
        )
        return res

    def decline_contact_request(self, userid: int, requesteduserid: int):
        res = self.moodle.post(
            'core_message_decline_contact_request',
            userid=userid,
            requesteduserid=requesteduserid,
        )
        return res

    def delete_contacts(self, userids: List[int], userid: int = 0):
        res = self.moodle.post(
            'core_message_delete_contacts',
            userids=userids,
            userid=userid,
        )
        return res

    def delete_conversation(self, userid: int, otheruserid: int):
        res = self.moodle.post(
            'core_message_delete_conversation',
            userid=userid,
            otheruserid=otheruserid,
        )
        return res

    def delete_conversations_by_id(self, userid: int,
                                   conversationids: List[int]):
        res = self.moodle.post(
            'core_message_delete_conversations_by_id',
            conversationids=conversationids,
        )
        return res

    def delete_message(self, messageid: int, userid: int, read: int = 1):
        res = self.moodle.post(
            'core_message_delete_message',
            messageid=messageid,
            userid=userid,
            read=read,
        )
        return res

    def delete_message_for_all_users(self, messageid: int, userid: int):
        res = self.moodle.post(
            'core_message_delete_message_for_all_users',
            messageid=messageid,
            userid=userid,
        )
        return res

    def get_blocked_users(self, userid: int):
        res = self.moodle.post('core_message_get_blocked_users', userid=userid)
        return res

    def get_contact_requests(self,
                             userid: int,
                             limitfrom: int = 0,
                             limitnum: int = 0):
        res = self.moodle.post(
            'core_message_get_contact_requests',
            userid=userid,
            limitfrom=limitfrom,
            limitnum=limitnum,
        )
        return res

    def get_contacts(self):
        res = self.moodle.post('core_message_get_contacts')
        return res

    def get_conversation(self,
                         userid: int,
                         conversationid: int,
                         includecontactrequests: int,
                         includeprivacyinfo: int,
                         memberlimit: int = 0,
                         memberoffset: int = 0,
                         messagelimit: int = 100,
                         messageoffset: int = 0,
                         newestmessagesfirst: int = 1):
        res = self.moodle.post(
            'core_message_get_conversation',
            userid=userid,
            conversationid=conversationid,
            includecontactrequests=includecontactrequests,
            includeprivacyinfo=includeprivacyinfo,
            memberlimit=memberlimit,
            memberoffset=memberoffset,
            messagelimit=messagelimit,
            messageoffset=messageoffset,
            newestmessagesfirst=newestmessagesfirst,
        )
        return res

    def get_conversation_between_users(self,
                                       userid: int,
                                       otheruserid: int,
                                       includecontactrequests: int,
                                       includeprivacyinfo: int,
                                       intmemberlimit: int = 0,
                                       memberoffset: int = 0,
                                       messagelimit: int = 100,
                                       messageoffset: int = 0,
                                       newestmessagesfirst: int = 1):
        res = self.moodle.post(
            'core_message_get_conversation_between_users',
            userid=userid,
            otheruserid=otheruserid,
            includecontactrequests=includecontactrequests,
            includeprivacyinfo=includeprivacyinfo,
            intmemberlimit=intmemberlimit,
            memberoffset=memberoffset,
            messagelimit=messagelimit,
            messageoffset=messageoffset,
            newestmessagesfirst=newestmessagesfirst,
        )
        return res

    def get_conversation_counts(self, userid: int = 0):
        res = self.moodle.post('core_message_get_conversation_counts',
                               userid=userid)
        return res

    def get_conversation_members(self,
                                 userid: int,
                                 conversationid: int,
                                 includecontactrequests: int,
                                 includeprivacyinfo: Optional[int] = None,
                                 limitfrom: int = 0,
                                 limitnum: int = 0):
        res = self.moodle.post(
            'core_message_get_conversation_members',
            userid=userid,
            conversationid=conversationid,
            includecontactrequests=includecontactrequests,
            includeprivacyinfo=includeprivacyinfo or '',
            limitfrom=limitfrom,
            limitnum=limitnum,
        )
        return res

    def get_conversation_messages(self,
                                  currentuserid: int,
                                  convid: int,
                                  limitfrom: int = 0,
                                  limitnum: int = 0,
                                  newest: Optional[int] = None,
                                  timefrom: Union[datetime, int] = 0):
        res = self.moodle.post(
            'core_message_get_conversation_messages',
            currentuserid=currentuserid,
            convid=convid,
            limitfrom=limitfrom,
            limitnum=limitnum,
            newest=newest or '',
            timefrom=timefrom,
        )
        return res

    def get_conversations(self,
                          userid: int,
                          limitfrom: int = 0,
                          limitnum: int = 0,
                          type_: Optional[int] = None):
        res = self.moodle.post(
            'core_message_get_conversations',
            userid=userid,
            limitfrom=limitfrom,
            limitnum=limitnum,
            type=type_,
        )
        return res

    def get_member_info(self,
                        referenceuserid: int,
                        userids: List[int],
                        includecontactrequests: Optional[int] = None,
                        includeprivacyinfo: Optional[int] = None):
        res = self.moodle.post(
            'core_message_get_member_info',
            referenceuserid=referenceuserid,
            userids=userids,
            includecontactrequests=includecontactrequests or '',
            includeprivacyinfo=includeprivacyinfo or '',
        )
        return res

    def get_messages(self,
                     useridto: int,
                     useridfrom: int = 0,
                     type_: str = 'both',
                     read: int = 1,
                     newestfirst: int = 1,
                     limitfrom: int = 0,
                     limitnum: int = 0):
        res = self.moodle.post(
            'core_message_get_messages',
            useridto=useridto,
            useridfrom=useridfrom,
            type=type_,
            read=read,
            newestfirst=newestfirst,
            limitfrom=limitfrom,
            limitnum=limitnum,
        )
        return res

    def get_received_contact_requests_count(self, userid: int):
        res = self.moodle.post(
            'core_message_get_received_contact_requests_count', userid=userid)
        return res

    def get_self_conversation(self,
                              userid: int,
                              messagelimit: int = 100,
                              messageoffset: int = 0,
                              newestmessagesfirst: int = 1):
        res = self.moodle.post(
            'core_message_get_self_conversation',
            userid=userid,
            messagelimit=messagelimit,
            messageoffset=messageoffset,
            newestmessagesfirst=newestmessagesfirst,
        )
        return res

    def get_unread_conversation_counts(self, userid: int = 0):
        res = self.moodle.post(
            'core_message_get_unread_conversation_counts',
            userid=userid,
        )
        return res

    def get_unread_conversations_count(self, useridto: int):
        res = self.moodle.post(
            'core_message_get_unread_conversations_count',
            useridto=useridto,
        )
        return res

    def get_user_contacts(self,
                          userid: int,
                          limitfrom: int = 0,
                          limitnum: int = 0):
        res = self.moodle.post(
            'core_message_get_user_contacts',
            userid=userid,
            limitfrom=limitfrom,
            limitnum=limitnum,
        )
        return res

    def get_user_message_preferences(self, userid: int = 0):
        res = self.moodle.post(
            'core_message_get_user_message_preferences',
            userid=userid,
        )
        return res

    def get_user_notification_preferences(self, userid: int = 0):
        res = self.moodle.post(
            'core_message_get_user_notification_preferences',
            userid=userid,
        )
        return res

    def mark_all_conversation_messages_as_read(self, userid: int,
                                               conversationid: int):
        res = self.moodle.post(
            'core_message_mark_all_conversation_messages_as_read',
            userid=userid,
            conversationid=conversationid,
        )
        return res

    def mark_all_messages_as_read(self, useridto: int, useridfrom: int = 0):
        res = self.moodle.post(
            'core_message_mark_all_messages_as_read',
            useridto=useridto,
            useridfrom=useridfrom,
        )
        return res

    def mark_all_notifications_as_read(self,
                                       useridto: int,
                                       useridfrom: int = 0):
        res = self.moodle.post(
            'core_message_mark_all_notifications_as_read',
            useridto=useridto,
            useridfrom=useridfrom,
        )
        return res

    def mark_message_read(self,
                          messageid: int,
                          timeread: Union[datetime, int] = 0):
        res = self.moodle.post(
            'core_message_mark_message_read',
            messageid=messageid,
            timeread=timeread,
        )
        return res

    def mark_notification_read(self,
                               notificationid: int,
                               timeread: Union[datetime, int] = 0):
        res = self.moodle.post(
            'core_message_mark_notification_read',
            notificationid=notificationid,
            timeread=timeread,
        )
        return res

    def message_processor_config_form(self, userid: int, name: str,
                                      formvalues: List[dict]):
        res = self.moodle.post(
            'core_message_message_processor_config_form',
            userid=userid,
            name=name,
            formvalues=formvalues,
        )
        return res

    def message_search_users(self,
                             userid: int,
                             search: str,
                             limitfrom: int = 0,
                             limitnum: int = 0):
        res = self.moodle.post(
            'core_message_message_search_users',
            userid=userid,
            search=search,
            limitfrom=limitfrom,
            limitnum=limitnum,
        )
        return res

    def mute_conversations(self, userid: int, conversationids: List[int]):
        res = self.moodle.post(
            'core_message_mute_conversations',
            userid=userid,
            conversationids=conversationids,
        )
        return res

    def search_contacts(self,
                        searchtext: str,
                        onlymycourses: Optional[int] = None):
        res = self.moodle.post(
            'core_message_search_contacts',
            searchtext=searchtext,
            onlymycourses=onlymycourses,
        )
        return res

    def send_instant_messages(self, messages: List[dict]):
        res = self.moodle.post(
            'core_message_send_instant_messages',
            messages=messages,
        )
        return res

    def send_messages_to_conversation(self, conversationid: int,
                                      messages: List[dict]):
        res = self.moodle.post(
            'core_message_send_messages_to_conversation',
            conversationid=conversationid,
            messages=messages,
        )
        return res

    def set_favourite_conversations(self, userid: int,
                                    conversations: List[int]):
        res = self.moodle.post(
            'core_message_set_favourite_conversations',
            userid=userid,
            conversations=conversations,
        )
        return res

    def unblock_contacts(self, userids: List[int], userid: int = 0):
        res = self.moodle.post(
            'core_message_unblock_contacts',
            userids=userids,
            userid=userid,
        )
        return res

    def unblock_user(self, userid: int, conversationids: List[int]):
        res = self.moodle.post(
            'core_message_unblock_user',
            userid=userid,
            conversationids=conversationids,
        )
        return res

    def unmute_conversations(self, userid: int, conversationids: List[int]):
        res = self.moodle.post(
            'core_message_unmute_conversations',
            userid=userid,
            conversationids=conversationids,
        )
        return res

    def unset_favourite_conversations(self,
                                      userid: int = 0,
                                      conversations: List[int] = None):
        res = self.moodle.post(
            'core_message_unset_favourite_conversations',
            userid=userid,
            conversations=conversations or [0],
        )
        return res
