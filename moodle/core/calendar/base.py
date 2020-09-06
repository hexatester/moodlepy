from datetime import datetime
from typing import List, Optional
from moodle import BaseMoodle
from moodle.utils.helper import from_dict
from . import Event, Events, CourseEvents


class BaseCalendar(BaseMoodle):
    def create_calendar_events(self, events: List[Event.Create]) -> Events:
        res = self.moodle.get('core_calendar_create_calendar_events',
                              events=events)
        return from_dict(Events, res)

    def delete_calendar_events(self, events: List[Event.Delete]) -> None:
        self.moodle.get('core_calendar_delete_calendar_events')
        return None

    def get_action_events_by_course(self,
                                    courseid: int,
                                    timesortfrom: Optional[datetime] = None,
                                    timesortto: Optional[datetime] = None,
                                    aftereventid: int = 0,
                                    limitnum: int = 20) -> CourseEvents:
        res = self.moodle.get('core_calendar_get_action_events_by_course')
        return from_dict(CourseEvents, res)

    def get_action_events_by_courses(self):
        res = self.moodle.get('core_calendar_get_action_events_by_courses')
        return res

    def get_action_events_by_timesort(self):
        res = self.moodle.get('core_calendar_get_action_events_by_timesort')
        return res

    def get_allowed_event_types(self):
        res = self.moodle.get('core_calendar_get_allowed_event_types')
        return res

    def get_calendar_access_information(self):
        res = self.moodle.get('core_calendar_get_calendar_access_information')
        return res

    def get_calendar_day_view(self):
        res = self.moodle.get('core_calendar_get_calendar_day_view')
        return res

    def get_calendar_event_by_id(self):
        res = self.moodle.get('core_calendar_get_calendar_event_by_id')
        return res

    def get_calendar_events(self):
        res = self.moodle.get('core_calendar_get_calendar_events')
        return res

    def get_calendar_monthly_view(self):
        res = self.moodle.get('core_calendar_get_calendar_monthly_view')
        return res

    def get_calendar_upcoming_view(self):
        res = self.moodle.get('core_calendar_get_calendar_upcoming_view')
        return res

    def get_timestamps(self):
        res = self.moodle.get('core_calendar_get_timestamps')
        return res

    def submit_create_update_form(self,
                                  formdata: str) -> CourseEvents.EventForm:
        """Submit form data for event form

        Args:
            formdata (str): The data from the event form

        Returns:
            CourseEvents.EventForm: Event form
        """
        res = self.moodle.get('core_calendar_submit_create_update_form')
        return from_dict(CourseEvents.EventForm, res)

    def update_event_start_day(self, eventid: int,
                               daytimestamp: datetime) -> Event:
        """Update the start day (but not time) for an event.

        Args:
            eventid (int): Id of event to be updated
            daytimestamp (datetime): Timestamp for the new start day

        Returns:
            Event: Updated event
        """
        res = self.moodle.get('core_calendar_update_event_start_day',
                              eventid=eventid,
                              daytimestamp=daytimestamp)
        return from_dict(Event, res['event'])
