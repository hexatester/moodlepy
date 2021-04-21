from datetime import datetime
from typing import List, Optional, Union

from moodle import BaseMoodle
from . import (
    AccessInformation,
    AllowedEventTypes,
    CalendarExportToken,
    Event,
    Events,
    CourseEvents,
    ActionEventCourses,
    DayView,
    MonthlyView,
    Timestamps,
)


class BaseCalendar(BaseMoodle):
    def create_calendar_events(self, events: List[Events.Create]) -> Events:
        """Create calendar events

        Args:
            events (List[Events.Create]): list of Events.Create

        Returns:
            Events: list of Event
        """
        res = self.moodle.post(
            "core_calendar_create_calendar_events",
            events=events,
        )
        return self._tr(Events, **res)

    def delete_calendar_events(self, events: List[Events.Delete]) -> None:
        """Delete calendar events

        Args:
            events (List[Events.Delete]): list of Events.Delete or list of {eventid:int, repeat:int}
        """
        self.moodle.post("core_calendar_delete_calendar_events", events=events)

    def get_action_events_by_course(
        self,
        courseid: int,
        timesortfrom: Union[datetime, int] = None,
        timesortto: Union[datetime, int] = None,
        aftereventid: int = 0,
        limitnum: int = 20,
    ) -> CourseEvents:
        """Get calendar action events by course

        Args:
            courseid (int): Course id
            timesortfrom (Union[datetime, int], optional): Time sort from. Defaults to None.
            timesortto (Union[datetime, int], optional): Time sort to. Defaults to None.
            aftereventid (int, optional): The last seen event id. Defaults to 0.
            limitnum (int, optional): Limit number. Defaults to 20.

        Returns:
            CourseEvents: list of CourseEvent
        """
        res = self.moodle.post(
            "core_calendar_get_action_events_by_course",
            courseid=courseid,
            timesortfrom=timesortfrom,
            timesortto=timesortto,
            aftereventid=aftereventid,
            limitnum=limitnum,
        )
        return self._tr(CourseEvents, **res)

    def get_action_events_by_courses(
        self,
        courseids: List[int],
        timesortfrom: Union[datetime, int] = None,
        timesortto: Union[datetime, int] = None,
        limitnum: int = 10,
    ) -> ActionEventCourses:
        """Get calendar action events by courses

        Args:
            courseids (List[int]): list of Course id
            timesortfrom (Union[datetime, int], optional): Time sort from. Defaults to None.
            timesortto (Union[datetime, int], optional): Time sort to. Defaults to None.
            limitnum (int, optional): Limit number. Defaults to 10.

        Returns:
            ActionEventCourses: list of CourseEvents
        """
        res = self.moodle.post(
            "core_calendar_get_action_events_by_courses",
            courseids=courseids,
            timesortfrom=timesortfrom,
            limitnum=limitnum,
        )
        return self._tr(ActionEventCourses, **res)

    def get_action_events_by_timesort(
        self,
        timesortfrom: Union[datetime, int] = 0,
        timesortto: Union[datetime, int] = None,
        aftereventid: int = 0,
        limitnum: int = 20,
        limittononsuspendedevents: int = None,
        userid: int = None,
    ) -> CourseEvents:
        """Get calendar action events by tiemsort

        Args:
            timesortfrom (Union[datetime, int], optional): Time sort from. Defaults to 0.
            timesortto (Union[datetime, int], optional): Time sort to. Defaults to None.
            aftereventid (int, optional): The last seen event id. Defaults to 0.
            limitnum (int, optional): Limit number. Defaults to 20.
            limittononsuspendedevents (int, optional): Limit the events to courses the user is not suspended in. Defaults to None.
            userid (int, optional): The user id. Defaults to None.

        Returns:
            CourseEvents: list of CourseEvent
        """
        res = self.moodle.post(
            "core_calendar_get_action_events_by_timesort",
            timesortfrom=timesortfrom,
            timesortto=timesortto,
            aftereventid=aftereventid,
            limitnum=limitnum,
            limittononsuspendedevents=limittononsuspendedevents,
            userid=userid,
        )
        return self._tr(CourseEvents, **res)

    def get_allowed_event_types(self, courseid: int = 0) -> AllowedEventTypes:
        """Get the type of events a user can create in the given course.

        Args:
            courseid (int, optional): Course to check, empty for site.. Defaults to 0.

        Returns:
            AllowedEventTypes: list of allowed event types to be created in the given course.
        """
        res = self.moodle.post(
            "core_calendar_get_allowed_event_types",
            courseid=courseid,
        )
        return self._tr(AllowedEventTypes, **res)

    def get_calendar_access_information(self, courseid: int = 0) -> AccessInformation:
        """Convenience function to retrieve some permissions/access information for the given course calendar.

        Args:
            courseid (int, optional): Course to check, empty for site calendar events. Defaults to 0.

        Returns:
            AccessInformation: Permissions/access information for the given course calendar
        """
        res = self.moodle.post(
            "core_calendar_get_calendar_access_information",
            courseid=courseid,
        )
        return self._tr(AccessInformation, **res)

    def get_calendar_day_view(
        self,
        year: int,
        month: int,
        day: int,
        courseid: int = 1,
        categoryid: Optional[int] = None,
    ) -> DayView:
        """Fetch the day view data for a calendar

        Args:
            year (int): Year to be viewed
            month (int): Month to be viewed
            day (int): Day to be viewed
            courseid (int, optional): Course being viewed. Defaults to 1.
            categoryid (Optional[int], optional): Category being viewed. Defaults to None.

        Returns:
            DayView: Response list of Event
        """
        res = self.moodle.post(
            "core_calendar_get_calendar_day_view",
            year=year,
            month=month,
            day=day,
            courseid=courseid,
            categoryid=categoryid,
        )
        return self._tr(DayView, **res)

    def get_calendar_event_by_id(self, eventid: int) -> CourseEvents:
        """Get calendar event by id

        Args:
            eventid (int): The event id to be retrieved

        Returns:
            CourseEvents: list of Event
        """
        res = self.moodle.post(
            "core_calendar_get_calendar_event_by_id",
            eventid=eventid,
        )
        return self._tr(CourseEvents, **res)

    def get_calendar_events(
        self, events: Events.Details = None, options: Events.Options = None
    ) -> Events:
        """Get calendar events

        Args:
            events (Events.Details, optional): Event details. Defaults to None.
            options (Events.Options, optional): Options. Defaults to None.

        Returns:
            Events: list of Event
        """
        res = self.moodle.post(
            "core_calendar_get_calendar_events",
            events=events if events else {},
            options=options if options else {},
        )
        return self._tr(Events, **res)

    def get_calendar_export_token(self) -> CalendarExportToken:
        """Return the auth token required for exporting a calendar.

        Returns:
            CalendarExportToken: The calendar permanent access token for calendar export.
        """
        res = self.moodle.post("core_calendar_get_calendar_export_token")
        return self._tr(CalendarExportToken, **res)

    def get_calendar_monthly_view(
        self,
        year: int,
        month: int,
        courseid: int = 1,
        categoryid: int = None,
        includenavigation: int = 1,
        mini: int = None,
        day: int = 1,
    ) -> MonthlyView:
        """Fetch the monthly view data for a calendar

        Args:
            year (int): Year to be viewed
            month (int): Month to be viewed
            courseid (int, optional): Course being viewed. Defaults to 1.
            categoryid (int, optional): Category being viewed. Defaults to None.
            includenavigation (int, optional): Whether to return the mini month view or not. Defaults to 1.
            mini (int, optional): Whether to return the mini month view or not. Defaults to None.
            day (int, optional): Day to be viewed. Defaults to 1.

        Returns:
            MonthlyView: [description]
        """
        res = self.moodle.post(
            "core_calendar_get_calendar_monthly_view",
            year=year,
            month=month,
            courseid=courseid,
            categoryid=categoryid,
            includenavigation=includenavigation,
            mini=mini,
            day=day,
        )
        return self._tr(MonthlyView, **res)

    def get_calendar_upcoming_view(
        self, courseid: int = 1, categoryid: int = None
    ) -> CourseEvents:
        """Fetch the upcoming view data for a calendar

        Args:
            courseid (int): Course being viewed. Defaults to 1.
            categoryid (int, optional): Category being viewed. Defaults to None.

        Returns:
            CourseEvents: [description]
        """
        res = self.moodle.post(
            "core_calendar_get_calendar_upcoming_view",
            courseid=courseid,
            categoryid=categoryid,
        )
        return self._tr(CourseEvents, **res)

    def get_timestamps(self, data: List[Timestamps.Create]) -> Timestamps:
        """Fetch unix timestamps for given date times.

        Args:
            data (List[Timestamps.Create]): list of Timestamps.Create

        Returns:
            Timestamps: list of Timestamp
        """
        res = self.moodle.post("core_calendar_get_timestamps", data=data)
        return self._tr(Timestamps, **res)

    def submit_create_update_form(self, formdata: str) -> CourseEvents.EventForm:
        """Submit form data for event form

        Args:
            formdata (str): The data from the event form

        Returns:
            CourseEvents.EventForm: Event form
        """
        res = self.moodle.post(
            "core_calendar_submit_create_update_form",
            formdata=formdata,
        )
        return self._tr(CourseEvents.EventForm, **res)

    def update_event_start_day(
        self, eventid: int, daytimestamp: Union[datetime, int]
    ) -> Event:
        """Update the start day (but not time) for an event.

        Args:
            eventid (int): Id of event to be updated
            daytimestamp (Union[datetime, int]): Timestamp for the new start day

        Returns:
            Event: Updated event
        """
        res = self.moodle.post(
            "core_calendar_update_event_start_day",
            eventid=eventid,
            daytimestamp=daytimestamp,
        )
        return Event(**res["event"])  # type: ignore
