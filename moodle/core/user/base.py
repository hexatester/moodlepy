from typing import List, Optional

from moodle import BaseMoodle, MoodleWarning
from . import (
    AgreeSitePolicyResponse,
    Criteria,
    CreateUser,
    GetUsersResponse,
    UserList,
    UserProfile,
)


class BaseUser(BaseMoodle):
    def add_user_device(self, appid: str, name: str, model: str, platform: str,
                        version: str, pushid: str,
                        uuid: str) -> List[Optional[List[MoodleWarning]]]:
        """Store mobile user devices information for PUSH Notifications.

        Args:
            appid (str): the app id, usually something like com.moodle.moodlemobile
            name (str): the device name, 'occam' or 'iPhone' etc.
            model (str): the device model 'Nexus4' or 'iPad1,1' etc.
            platform (str): the device platform 'iOS' or 'Android' etc.
            version (str): the device platform 'iOS' or 'Android' etc.
            pushid (str): the device version '6.1.2' or '4.2.2' etc.
            uuid (str): the device PUSH token/key/identifier/registration id

        Returns:
            List[Optional[List[Warning]]]: Response
        """
        results: List[Optional[List[MoodleWarning]]] = list()
        data = self.moodle.post(
            'core_user_add_user_device',
            appid=appid,
            name=name,
            model=model,
            platform=platform,
            version=version,
            pushid=pushid,
            uuid=uuid,
        )
        if not data:
            return results
        for dat in data:
            results.append([MoodleWarning(**da) for da in dat])  # type: ignore
        return results

    def add_user_private_files(self, draftid: int):
        """Copy files from a draft area to users private files area.

        Args:
            draftid (int): draft area id

        Returns:
            None: No response
        """
        data = self.moodle.post(
            'core_user_add_user_private_files',
            draftid=draftid,
        )
        return data

    def agree_site_policy(self) -> AgreeSitePolicyResponse:
        """Agree the site policy for the current user.

        Returns:
            AgreeSitePolicyResponse: Response
        """
        data = self.moodle.post('core_user_agree_site_policy')
        return self._tr(AgreeSitePolicyResponse, **data)

    def create_users(self,
                     users: List[CreateUser]) -> List[CreateUser.Response]:
        """Create users.

        Args:
            users (List[CreateUser]): list of CreateUser

        Returns:
            List[CreateUser.Response]: list of created user id and user name
        """
        data = self.moodle.post(
            'core_user_create_users',
            users=users,
        )
        return [CreateUser.Response(**dat) for dat in data]  # type: ignore

    def delete_users(self, userids: List[int]) -> None:
        """Delete users.

        Args:
            userids (List[int]): list of user ID

        Returns:
            None: None
        """
        data = self.moodle.post(
            'core_user_delete_users',
            userids=userids,
        )
        return data

    def get_course_user_profiles(
            self, userlist: List[UserList]) -> List[UserProfile]:
        """Get course user profiles (each of the profils matching a course id and a user id),.

        Args:
            userlist (List[UserList]): list of UserList or dict containing userid and courseid

        Returns:
            List[UserProfile]: list of UserProfile
        """
        data = self.moodle.post(
            'core_user_get_course_user_profiles',
            userlist=userlist,
        )
        return [UserProfile(**dat) for dat in data]  # type: ignore

    def get_private_files_info(self):
        data = self.moodle.post('core_user_get_private_files_info')
        return data

    def get_user_preferences(self):
        data = self.moodle.post('core_user_get_user_preferences')
        return data

    def get_users(self, criteria: List[Criteria]) -> GetUsersResponse:
        """search for users matching the parameters

        Args:
            criteria (List[Criteria]): the key/value pairs to be considered in user search.
                                        Values can not be empty. Specify different keys only once (fullname => 'user1', auth => 'manual', ...) - key occurences are forbidden.
                                        The search is executed with AND operator on the criterias. Invalid criterias (keys) are ignored, the search is still executed on the valid criterias.
                                        You can search without criteria, but the function is not designed for it. It could very slow or timeout.
                                        The function is designed to search some specific users.

        Returns:
            GetUsersResponse: Response
        """
        data = self.moodle.post(
            'core_user_get_users',
            criteria=criteria,
        )
        return self._tr(GetUsersResponse, **data)

    def get_users_by_field(self):
        data = self.moodle.post('core_user_get_users_by_field')
        return data

    def remove_user_device(self):
        data = self.moodle.post('core_user_remove_user_device')
        return data

    def set_user_preferences(self):
        data = self.moodle.post('core_user_set_user_preferences')
        return data

    def update_picture(self):
        data = self.moodle.post('core_user_update_picture')
        return data

    def update_user_preferences(self):
        data = self.moodle.post('core_user_update_user_preferences')
        return data

    def update_users(self):
        data = self.moodle.post('core_user_update_users')
        return data

    def view_user_list(self):
        data = self.moodle.post('core_user_view_user_list')
        return data

    def view_user_profile(self):
        data = self.moodle.post('core_user_view_user_profile ')
        return data
