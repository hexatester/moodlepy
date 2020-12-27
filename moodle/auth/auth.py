from moodle import BaseMoodle
from moodle.utils.decorator import lazy_property
from . import BaseEmail


class Auth(BaseMoodle):
    @lazy_property
    def email(self) -> BaseEmail:
        return BaseEmail(self.moodle)

    @property
    def confirm_user(self):
        data = self.moodle.get('core_auth_confirm_user')
        return data

    @property
    def is_age_digital_consent_verification_enabled(self):
        data = self.moodle.get(
            'core_auth_is_age_digital_consent_verification_enabled')
        return data

    @property
    def is_minor(self):
        data = self.moodle.get('core_auth_is_minor')
        return data

    @property
    def request_password_reset(self):
        data = self.moodle.get('core_auth_request_password_reset')
        return data

    @property
    def resend_confirmation_email(self):
        data = self.moodle.get('core_auth_resend_confirmation_email')
        return data
