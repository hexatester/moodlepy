from moodle import Moodle
from moodle.core.course import Course


class TestCourse:
    def test_get_courses(self, moodle: Moodle):
        courses = moodle.core.course.get_courses()
        assert type(courses) == list
        for course in courses:
            assert isinstance(course, Course)
            assert type(course.id) == int
            assert type(course.shortname) == str
            assert type(course.categoryid) == int
            assert type(course.categorysortorder) == int
            assert type(course.fullname) == str
            assert type(course.displayname) == str
            assert type(course.idnumber) == str
            assert type(course.summary) == str
            assert type(course.summaryformat) == int
            assert type(course.format) == str
            assert type(course.showgrades) == int
            assert type(course.newsitems) == int
            assert type(course.startdate) == int
            assert type(course.enddate) == int
            assert type(course.numsections) == int
            assert type(course.maxbytes) == int
            assert type(course.showreports) == int
            assert type(course.visible) == int
            assert type(course.groupmode) == int
            assert type(course.groupmodeforce) == int
            assert type(course.defaultgroupingid) == int
            assert type(course.enablecompletion) == int
            assert type(course.completionnotify) == int
            assert type(course.lang) == str
            assert type(course.forcetheme) == str
