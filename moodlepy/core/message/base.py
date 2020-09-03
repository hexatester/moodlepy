from dacite import from_dict
from moodlepy import BaseMoodle, MessagePreference, NotificationPreference


class BaseMessage(BaseMoodle):
    def core_message_get_user_message_preferences(self) -> MessagePreference:
        data = self.moodle.get('core_message_get_user_message_preferences')
        return from_dict(MessagePreference, data)

    def get_user_notification_preferences(self) -> NotificationPreference:
        data = self.moodle.get(
            'core_message_get_user_notification_preferences')
        return from_dict(NotificationPreference, data)
