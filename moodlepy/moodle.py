from requests import Session
from typing import Any
from moodlepy import Mod


class Moodle:
    session: Session = Session()
    token: str = ''
    url: str = ''

    def __init__(self, url: str, token: str):
        self.url = url
        self.token = token
        self._mod = Mod(self)

    def __call__(self,
                 wsfunction: str,
                 moodlewsrestformat='json',
                 **kwargs) -> Any:
        return self.get(wsfunction, moodlewsrestformat, **kwargs)

    @property
    def mod(self) -> Mod:
        return self._mod

    def get(self, wsfunction: str, moodlewsrestformat='json', **kwargs) -> Any:
        params = {
            'wstoken': self.token,
            'wsfunction': wsfunction,
            'moodlewsrestformat': moodlewsrestformat
        }
        params.update(kwargs)
        res = self.session.get(self.url, params=params)
        if res.ok and moodlewsrestformat == 'json':
            return res.json()
