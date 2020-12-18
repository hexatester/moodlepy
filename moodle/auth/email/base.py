from moodle import BaseMoodle
from moodle.utils.helper import from_dict
from . import SignupSetting


class BaseEmail(BaseMoodle):
    def get_signup_setting(self) -> SignupSetting:
        """Get the signup required settings and profile fields.

        Returns:
            SignupSetting: Signup required settings and profile fields
        """
        data = self.moodle.get('auth_email_get_signup_setting')
        return from_dict(SignupSetting, data)

    def signup_user(self):
        # TODO auth_email_get_signup_setting
        raise NotImplementedError(
            'auth_email_get_signup_setting not implemented yet')
        data = self.moodle.get('auth_email_signup_user')
        return data
