from moodle import BaseMoodle, BaseEmail


class Auth(BaseMoodle):
    def __post_init__(self, moodle) -> None:
        self._email = BaseEmail(moodle)

    @property
    def email(self) -> BaseEmail:
        return self._email
