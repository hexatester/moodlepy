from __future__ import annotations
import logging
import requests
from dacite import from_dict
from requests import Session
from typing import Any, Optional
from moodle import Auth, Core, Mod, MoodleException, Tool, Warning


class Moodle:
    session: Session = Session()
    token: str = ''
    url: str = ''

    def __init__(self, url: str, token: str):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.url = url
        self.token = token
        self._auth = Auth(self)
        self._core = Core(self)
        self._mod = Mod(self)
        self._tool = Tool(self)

    def __call__(self,
                 wsfunction: str,
                 moodlewsrestformat='json',
                 **kwargs) -> Any:
        return self.get(wsfunction, moodlewsrestformat, **kwargs)

    @property
    def auth(self) -> Auth:
        return self._auth

    @property
    def core(self) -> Core:
        return self._core

    @property
    def mod(self) -> Mod:
        return self._mod

    @property
    def tool(self) -> Tool:
        return self._tool

    def get(self, wsfunction: str, moodlewsrestformat='json', **kwargs) -> Any:
        params = {
            'wstoken': self.token,
            'wsfunction': wsfunction,
            'moodlewsrestformat': moodlewsrestformat
        }
        params.update(kwargs)
        res = self.session.get(self.url, params=params)
        if res.ok and moodlewsrestformat == 'json':
            data = res.json()
            if type(data) == dict:
                if 'warnings' in data:
                    warning = from_dict(Warning, data['warnings'])
                    self.logger.warning(str(warning))
                if 'exception' in data or 'errorcode' in data:
                    raise from_dict(MoodleException, data)
            return data
        return res.text

    @classmethod
    def login(
        cls,
        domain: str,
        username: str,
        password: str,
        service: str = 'moodle_mobile_app',
        loginurl: str = '/login/token.php',
        web_service_url: str = '/webservice/rest/server.php'
    ) -> Optional[Moodle]:
        domain = domain.lstrip('/')
        params = {
            'username': username,
            'password': password,
            'service': service
        }
        url = loginurl if loginurl.startswith(domain) else domain + loginurl
        res = requests.get(url, params=params)
        if not res.ok:
            return None
        data = res.json()
        if 'token' in data:
            return cls(url=web_service_url
                       if web_service_url.startswith(domain) else domain +
                       web_service_url,
                       token=data['token'])
        return None
