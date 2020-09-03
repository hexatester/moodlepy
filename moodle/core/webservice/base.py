from __future__ import annotations
from dacite import from_dict
from moodle import BaseMoodle, SiteInfo


class BaseWebservice(BaseMoodle):
    def get_site_info(self) -> SiteInfo:
        data = self.moodle.get('core_webservice_get_site_info')
        if data:
            return from_dict(SiteInfo, data)
        raise Exception('Info not found')
