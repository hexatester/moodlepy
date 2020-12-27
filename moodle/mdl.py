from __future__ import annotations
import logging
import requests
from requests import Session
from requests.exceptions import RequestException
from typing import Any, Type, TypeVar
from moodle import Auth, Core, Mod, MoodleException, Tool, MoodleWarning
from moodle.exception import EmptyResponseException, InvalidCredentialException, NetworkMoodleException
from moodle.utils.helper import make_params, from_dict, to_dict

T = TypeVar('T', bound='Mdl')


class Mdl:
    session: Session = Session()
    token: str = ''
    url: str = ''

    def __init__(self, url: str, token: str):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.url = url
        self.token = token

    def get(self, wsfunction: str, moodlewsrestformat='json', **kwargs) -> Any:
        params = make_params(self.token, wsfunction, moodlewsrestformat)
        params.update(to_dict(kwargs))
        res = self.session.get(self.url, params=params)
        if res.ok and moodlewsrestformat == 'json':
            data = res.json()
            return self.process_response(data)
        return res.text

    def post(self,
             wsfunction: str,
             moodlewsrestformat='json',
             **kwargs: Any) -> Any:
        params = make_params(self.token, wsfunction, moodlewsrestformat)
        try:
            res = self.session.post(self.url,
                                    data=to_dict(kwargs),
                                    params=params)
        except RequestException as e:
            raise NetworkMoodleException(e)
        if not res.ok or not res.text:
            raise EmptyResponseException()
        if res.ok and moodlewsrestformat == 'json':
            data = res.json()
            return self.process_response(data)
        return res.text

    def process_response(self, data: Any) -> Any:
        if type(data) == dict:
            if 'warnings' in data and data['warnings']:
                warning = from_dict(MoodleWarning, data['warnings'])
                self.logger.warning(str(warning))
            if 'exception' in data or 'errorcode' in data:
                raise from_dict(MoodleException, data)
        return data

    @classmethod
    def login(cls: Type[T],
              domain: str,
              username: str,
              password: str,
              service: str = 'moodle_mobile_app',
              loginurl: str = '/login/token.php',
              web_service_url: str = '/webservice/rest/server.php') -> T:
        """Get a Moodle instance by using username & password auth

        Args:
            domain (str): The domain of moodle app
            username (str): Username
            password (str): Password
            service (str, optional): Service name. Defaults to 'moodle_mobile_app'.
            loginurl (str, optional): Url to get token from. Defaults to '/login/token.php'.
            web_service_url (str, optional): Moodle Web Service endpoint. Defaults to '/webservice/rest/server.php'.

        Raises:
            InvalidCredentialException: Wrong credential

        Returns:
            Moodle: Returns an instance of Moodle
        """
        data = cls.get_tokens(domain, username, password, service, loginurl)
        if 'token' not in data:
            raise InvalidCredentialException()
        return cls(url=web_service_url if web_service_url.startswith(domain)
                   else domain + web_service_url,
                   token=data['token'])

    @classmethod
    def get_tokens(
        cls,
        domain: str,
        username: str,
        password: str,
        service: str = 'moodle_mobile_app',
        loginurl: str = '/login/token.php',
    ) -> dict:
        domain = domain.lstrip('/')
        params = {
            'username': username,
            'password': password,
            'service': service
        }
        url = loginurl if loginurl.startswith(domain) else domain + loginurl
        res = requests.get(url, params=params)
        return res.json() if res.ok else {}


class Moodle(Mdl):
    def __init__(self, url: str, token: str):
        super(Moodle, self).__init__(url, token)
        self._auth = Auth(self)
        self._core = Core(self)
        self._mod = Mod(self)
        self._tool = Tool(self)

    def __call__(self,
                 wsfunction: str,
                 moodlewsrestformat='json',
                 **kwargs) -> Any:
        return self.post(wsfunction, moodlewsrestformat, **kwargs)

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
