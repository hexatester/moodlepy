from moodlepy import Forum


class Mod:
    def __init__(self, moodle):
        self._moodle = moodle
        self._forum = Forum.inject(self.moodle)

    @property
    def moodle(self):
        return self._moodle

    @property
    def forum(self) -> Forum:
        return self._forum
