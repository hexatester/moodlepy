from datetime import datetime
from typing import List, Optional, Union

from moodle import BaseMoodle
from . import (
    AccessInformation,
    AllowedEventTypes,
    Event,
    Events,
    CourseEvents,
    ActionEventCourses,
    DayView,
    MonthlyView,
)


class BaseCalendar(BaseMoodle):
    def create_calendar_events(self, events: List[Events.Create]) -> Events:
        res = self.moodle.get('core_calendar_create_calendar_events',
                              events=events)
        return self._tr(Events, **res)

    def delete_calendar_events(self, events: List[Events.Delete]) -> None:
        self.moodle.get('core_calendar_delete_calendar_events')
        return None

    def get_action_events_by_course(self,
                                    courseid: int,
                                    timesortfrom: Optional[Union[datetime,
                                                                 int]] = None,
                                    timesortto: Optional[Union[datetime,
                                                               int]] = None,
                                    aftereventid: int = 0,
                                    limitnum: int = 20) -> CourseEvents:
        res = self.moodle.get('core_calendar_get_action_events_by_course',
                              courseid=courseid,
                              timesortfrom=timesortfrom,
                              timesortto=timesortto,
                              aftereventid=aftereventid,
                              limitnum=limitnum)
        return self._tr(CourseEvents, **res)

    def get_action_events_by_courses(self,
                                     courseids: List[int],
                                     timesortfrom: Optional[Union[datetime,
                                                                  int]] = None,
                                     timesortto: Optional[Union[datetime,
                                                                int]] = None,
                                     limitnum: int = 10) -> ActionEventCourses:
        res = self.moodle.get('core_calendar_get_action_events_by_courses',
                              courseids=courseids,
                              timesortfrom=timesortfrom,
                              limitnum=limitnum)
        return self._tr(ActionEventCourses, **res)

    def get_action_events_by_timesort(
            self,
            timesortfrom: Optional[Union[datetime, int]] = 0,
            timesortto: Optional[Union[datetime, int]] = None,
            aftereventid: int = 0,
            limitnum: int = 20,
            limittononsuspendedevents: Optional[int] = None,
            userid: Optional[int] = None) -> CourseEvents:
        res = self.moodle.get(
            'core_calendar_get_action_events_by_timesort',
            timesortfrom=timesortfrom,
            timesortto=timesortto,
            aftereventid=aftereventid,
            limitnum=limitnum,
            limittononsuspendedevents=limittononsuspendedevents,
            userid=userid,
        )
        return self._tr(CourseEvents, **res)

    def get_allowed_event_types(self, courseid: int = 0) -> AllowedEventTypes:
        res = self.moodle.get('core_calendar_get_allowed_event_types',
                              courseid=courseid)
        return self._tr(AllowedEventTypes, **res)

    def get_calendar_access_information(self,
                                        courseid: int = 0
                                        ) -> AccessInformation:
        res = self.moodle.get('core_calendar_get_calendar_access_information',
                              courseid=courseid)
        return self._tr(AccessInformation, **res)

    def get_calendar_day_view(self,
                              year: int,
                              month: int,
                              day: int,
                              courseid: int = 1,
                              categoryid: Optional[int] = None) -> DayView:
        res = self.moodle.get(
            'core_calendar_get_calendar_day_view',
            year=year,
            month=month,
            day=day,
            courseid=courseid,
            categoryid=categoryid,
        )
        return self._tr(DayView, **res)

    def get_calendar_event_by_id(self, eventid: int) -> CourseEvents:
        res = self.moodle.get('core_calendar_get_calendar_event_by_id',
                              eventid=eventid)
        return self._tr(CourseEvents, **res)

    def get_calendar_events(
            self,
            events: Optional[Events.Details] = None,
            options: Optional[Events.Options] = None) -> Events:
        res = self.moodle.get('core_calendar_get_calendar_events',
                              events=events if events else {},
                              options=options if options else {})
        return self._tr(Events, **res)

    def get_calendar_monthly_view(self,
                                  year: int,
                                  month: int,
                                  courseid: int = 1,
                                  categoryid: Optional[int] = None,
                                  includenavigation: int = 1,
                                  mini: Optional[int] = None) -> MonthlyView:
        res = self.moodle.get('core_calendar_get_calendar_monthly_view')
        return self._tr(MonthlyView, **res)

    def get_calendar_upcoming_view(
            self,
            courseid: int,
            categoryid: Optional[int] = None) -> CourseEvents:
        res = self.moodle.get('core_calendar_get_calendar_upcoming_view')
        return self._tr(CourseEvents, **res)

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
        return self._tr(CourseEvents.EventForm, **res)

    def update_event_start_day(self, eventid: int,
                               daytimestamp: Union[datetime, int]) -> Event:
        """Update the start day (but not time) for an event.

        Args:
            eventid (int): Id of event to be updated
            daytimestamp (Union[datetime, int]): Timestamp for the new start day

        Returns:
            Event: Updated event
        """
        res = self.moodle.get('core_calendar_update_event_start_day',
                              eventid=eventid,
                              daytimestamp=daytimestamp)
        return Event(**res['event'])  # type: ignore
