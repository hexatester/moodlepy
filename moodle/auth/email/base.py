from moodle import BaseMoodle


class BaseEmail(BaseMoodle):
    def get_signup_setting(self):
        # TODO auth_email_get_signup_setting
        raise NotImplementedError(
            'auth_email_get_signup_setting not implemented yet')
        data = self.moodle.get('auth_email_get_signup_setting')
        return data

    def signup_user(self):
        # TODO auth_email_get_signup_setting
        raise NotImplementedError(
            'auth_email_get_signup_setting not implemented yet')
        data = self.moodle.get('auth_email_signup_user')
        return data
