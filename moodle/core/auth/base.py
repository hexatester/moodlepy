from moodle import BaseMoodle
from moodle.base.general import GeneralSuccess
from . import RequestPasswordResetResponse


class BaseAuth(BaseMoodle):
    def confirm_user(self, username: str, secret: str) -> GeneralSuccess:
        """Confirm a user account.

        Args:
            username (str): User name
            secret (str): Confirmation secret

        Returns:
            GeneralSuccess: True if the user was confirmed, false if he was already confirmed
        """
        data = self.moodle.post(
            "core_auth_confirm_user",
            username=username,
            secret=secret,
        )
        return self._tr(GeneralSuccess, **data)

    def is_age_digital_consent_verification_enabled(self) -> GeneralSuccess:
        """Checks if age digital consent verification is enabled.

        Returns:
            GeneralSuccess: True if digital consent verification is enabled, false otherwise.
        """
        data = self.moodle.post("core_auth_is_age_digital_consent_verification_enabled")
        return self._tr(GeneralSuccess, **data)

    def is_minor(self, age: int, country: str) -> GeneralSuccess:
        """Requests a check if a user is a digital minor.

        Args:
            age (int): Age
            country (str): Country of residence

        Returns:
            GeneralSuccess: True if the user is considered to be a digital minor, false if not
        """
        data = self.moodle.post(
            "core_auth_is_minor",
            age=age,
            country=country,
        )
        return self._tr(GeneralSuccess, **data)

    def request_password_reset(
        self, username: str = "", email: str = ""
    ) -> RequestPasswordResetResponse:
        """Requests a password reset.

        Args:
            username (str, optional): User name. Defaults to ''.
            email (str, optional): User email. Defaults to ''.

        Returns:
            RequestPasswordResetResponse: Response
        """
        data = self.moodle.post(
            "core_auth_request_password_reset",
            username=username,
            email=email,
        )
        return self._tr(RequestPasswordResetResponse, **data)

    def resend_confirmation_email(
        self, username: str, password: str, redirect: str = ""
    ) -> GeneralSuccess:
        data = self.moodle.post(
            "core_auth_resend_confirmation_email",
            username=username,
            password=password,
            redirect=redirect,
        )
        return self._tr(GeneralSuccess, **data)
