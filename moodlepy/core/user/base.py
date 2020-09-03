from dacite import from_dict
from moodlepy import BaseMoodle, UserPreference


class BaseUser(BaseMoodle):
    def get_user_preferences(self) -> UserPreference:
        data = self.moodle.get('core_user_get_user_preferences')
        return from_dict(UserPreference, data)
