from moodlepy import BaseMoodle, BaseWebservice


class Core(BaseMoodle):
    def __post_init__(self, moodle) -> None:
        self._webservice = BaseWebservice(moodle)

    @property
    def webservice(self) -> BaseWebservice:
        return self._webservice
