from typing import List, Optional
from moodle import BaseMoodle
from moodle.utils.typing import Array
from . import SignupSetting, SignupUserResponse, UserCustomField


class BaseEmail(BaseMoodle):
    def get_signup_setting(self) -> SignupSetting:
        """Get the signup required settings and profile fields.

        Returns:
            SignupSetting: Signup required settings and profile fields
        """
        data = self.moodle.get('auth_email_get_signup_setting')
        return self._tr(SignupSetting, **data)

    def signup_user(self,
                    username: str,
                    password: str,
                    firstname: str,
                    lastname: str,
                    email: str,
                    city: str = '',
                    country: str = '',
                    recaptchachallengehash: str = '',
                    recaptcharesponse: str = '',
                    customprofilefields: Optional[
                        List[UserCustomField]] = None,
                    redirect: str = '') -> SignupUserResponse:
        """Adds a new user (pendingto be confirmed) in the site.

        Args:
            username (str): Username
            password (str): Plain text password
            firstname (str): The first name(s) of the user
            lastname (str): The family name of the user
            email (str): A valid and unique email address
            city (str, optional): Home city of the user. Defaults to ''.
            country (str, optional): Home country code. Defaults to ''.
            recaptchachallengehash (str, optional): Recaptcha challenge hash. Defaults to ''.
            recaptcharesponse (str, optional): Recaptcha response. Defaults to ''.
            customprofilefields (Optional[ List[UserCustomField]], optional): User custom fields (also known as user profile fields). Defaults to None.
            redirect (str, optional): Redirect the user to this site url after confirmation.. Defaults to ''.

        Returns:
            SignupUserResponse: Response
        """
        customprofilefields = Array(
            customprofilefields if customprofilefields else [])
        customprofilefields.name = 'customprofilefields'
        data = self.moodle.get(
            'auth_email_signup_user',
            username=username,
            password=password,
            firstname=firstname,
            lastname=lastname,
            email=email,
            city=city,
            country=country,
            recaptchachallengehash=recaptchachallengehash,
            recaptcharesponse=recaptcharesponse,
            customprofilefields=customprofilefields,
            redirect=redirect,
        )
        return self._tr(SignupUserResponse, **data)
