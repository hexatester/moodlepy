from moodlepy import BaseMoodle, BaseMessage, BaseWebservice


class Core(BaseMoodle):
    def __post_init__(self, moodle) -> None:
        self._message = BaseMessage(moodle)
        self._webservice = BaseWebservice(moodle)

    @property
    def message(self) -> BaseMessage:
        return self._message

    @property
    def webservice(self) -> BaseWebservice:
        return self._webservice
