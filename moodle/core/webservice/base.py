from __future__ import annotations
from moodle import BaseMoodle
from . import SiteInfo


class BaseWebservice(BaseMoodle):
    def get_site_info(self) -> SiteInfo:
        data = self.moodle.get('core_webservice_get_site_info')
        if data:
            return SiteInfo(**data)  # type: ignore
        raise Exception('Info not found')
