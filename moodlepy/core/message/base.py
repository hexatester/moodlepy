from dacite import from_dict
from typing import Optional
from moodlepy import BaseMoodle, NotificationPreference


class BaseMessage(BaseMoodle):
    def get_user_notification_preferences(
            self) -> Optional[NotificationPreference]:
        datas = self.moodle.get(
            'core_message_get_user_notification_preferences')
        if not datas or 'preferences' not in datas:
            return None
        data = datas['preferences']
        return from_dict(NotificationPreference, data)
