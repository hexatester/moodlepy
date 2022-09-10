import cattr
import logging
import requests

try:
    import ujson as json
except ImportError:
    import json  # type: ignore[no-redef]
from datetime import datetime
from requests import Session
from requests.exceptions import RequestException
from typing import Any, Dict, Union

from moodle import __version__
from moodle import MoodleException
from moodle import MoodleWarning

from moodle.exception import (
    EmptyResponseException,
    InvalidCredentialException,
    NetworkMoodleException,
)
from moodle.utils.helper import make_params, to_dict, fromtimestamp


class Mdl:
    session: Session = Session()
    token: str = ""
    url: str = ""
    __headers__: Dict[str, str] = {"User-Agent": f"moodlepy-{__version__}"}

    def __init__(self, url: str, token: str, user_agent: str = None):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.url = url
        self.token = token
        if user_agent:
            self.__headers__["User-Agent"] = user_agent
        self.session.headers.update(self.__headers__)
        cattr.register_structure_hook(datetime, lambda d, t: fromtimestamp(d))
        cattr.register_structure_hook(Union[str, int], lambda d, t: d)

    def get(self, wsfunction: str, moodlewsrestformat="json", **kwargs) -> Any:
        params = make_params(self.token, wsfunction, moodlewsrestformat)
        params.update(to_dict(kwargs))
        res = self.session.get(self.url, params=params)
        if res.ok and moodlewsrestformat == "json":
            data = json.loads(res.text)
            return self.process_response(data)
        return res.text

    def post(self, wsfunction: str, moodlewsrestformat="json", **kwargs: Any) -> Any:
        params = make_params(self.token, wsfunction, moodlewsrestformat)
        try:
            res = self.session.post(
                self.url,
                data=to_dict(kwargs),
                params=params,
            )
        except RequestException as e:
            raise NetworkMoodleException(e)
        if not res.ok or not res.text:
            raise EmptyResponseException()
        if res.ok and moodlewsrestformat == "json":
            data = json.loads(res.text)
            return self.process_response(data)
        return res.text

    def process_response(self, data: Any) -> Any:
        if isinstance(data, dict):
            if "warnings" in data and data["warnings"]:
                if isinstance(data["warnings"], list):
                    for warn in data["warnings"]:
                        warning = MoodleWarning(**warn)  # type: ignore
                        self.logger.warning(str(warning))
                elif isinstance(data["warnings"], dict):
                    warning = MoodleWarning(**data["warnings"])  # type: ignore
                    self.logger.warning(str(warning))
            if "exception" in data or "errorcode" in data:
                raise MoodleException(**data)  # type: ignore
        return data

    @classmethod
    def login(
        cls,
        domain: str,
        username: str,
        password: str,
        service: str = "moodle_mobile_app",
        loginurl: str = "/login/token.php",
        web_service_url: str = "/webservice/rest/server.php",
    ):
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
        if "token" not in data:
            raise InvalidCredentialException()
        return cls(
            url=web_service_url
            if web_service_url.startswith(domain)
            else domain + web_service_url,
            token=data["token"],
        )

    @classmethod
    def get_tokens(
        cls,
        domain: str,
        username: str,
        password: str,
        service: str = "moodle_mobile_app",
        loginurl: str = "/login/token.php",
    ) -> dict:
        domain = domain.lstrip("/")
        params = {"username": username, "password": password, "service": service}
        url = loginurl if loginurl.startswith(domain) else domain + loginurl
        res = requests.get(url, params=params)
        return json.loads(res.text) if res.ok else {}
