from dacite import from_dict
from typing import List
from moodlepy import BaseMoodle, MobilePlugin, MobilePublicConfig


class BaseMobile(BaseMoodle):
    def get_plugins_supporting_mobile(self) -> List[MobilePlugin]:
        datas = self.moodle.get('tool_mobile_get_plugins_supporting_mobile')
        return [from_dict(MobilePlugin, data)
                for data in datas['plugins']] if 'plugins' in datas else []

    def get_public_config(self) -> MobilePublicConfig:
        data = self.moodle.get('tool_mobile_get_public_config')
        return from_dict(MobilePublicConfig, data)
