from dacite import from_dict
from typing import List
from moodle import BaseMoodle
from . import MobileConfig, MobilePlugin, MobilePublicConfig


class BaseMobile(BaseMoodle):
    def get_config(self) -> MobileConfig:
        data = self.moodle.get('tool_mobile_get_config')
        return from_dict(MobileConfig, data)

    def get_plugins_supporting_mobile(self) -> List[MobilePlugin]:
        datas = self.moodle.get('tool_mobile_get_plugins_supporting_mobile')
        return [from_dict(MobilePlugin, data)
                for data in datas['plugins']] if 'plugins' in datas else []

    def get_public_config(self) -> MobilePublicConfig:
        data = self.moodle.get('tool_mobile_get_public_config')
        return from_dict(MobilePublicConfig, data)
