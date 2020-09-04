from moodle import BaseMoodle


class BaseCalendar(BaseMoodle):
    def create_calendar_events(self):
        data = self.moodle.get('core_calendar_create_calendar_events')
        return data

    def delete_calendar_events(self):
        data = self.moodle.get('core_calendar_delete_calendar_events')
        return data

    def get_action_events_by_course(self):
        data = self.moodle.get('core_calendar_get_action_events_by_course')
        return data

    def get_action_events_by_courses(self):
        data = self.moodle.get('core_calendar_get_action_events_by_courses')
        return data

    def get_action_events_by_timesort(self):
        data = self.moodle.get('core_calendar_get_action_events_by_timesort')
        return data

    def get_allowed_event_types(self):
        data = self.moodle.get('core_calendar_get_allowed_event_types')
        return data

    def get_calendar_access_information(self):
        data = self.moodle.get('core_calendar_get_calendar_access_information')
        return data

    def get_calendar_day_view(self):
        data = self.moodle.get('core_calendar_get_calendar_day_view')
        return data

    def get_calendar_event_by_id(self):
        data = self.moodle.get('core_calendar_get_calendar_event_by_id')
        return data

    def get_calendar_events(self):
        data = self.moodle.get('core_calendar_get_calendar_events')
        return data

    def get_calendar_monthly_view(self):
        data = self.moodle.get('core_calendar_get_calendar_monthly_view')
        return data

    def get_calendar_upcoming_view(self):
        data = self.moodle.get('core_calendar_get_calendar_upcoming_view')
        return data

    def get_timestamps(self):
        data = self.moodle.get('core_calendar_get_timestamps')
        return data

    def submit_create_update_form(self):
        data = self.moodle.get('core_calendar_submit_create_update_form')
        return data

    def update_event_start_day(self):
        data = self.moodle.get('core_calendar_update_event_start_day')
        return data
