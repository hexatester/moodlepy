from moodle import Moodle
from moodle.core.course import Course, Category


class TestCourse:
    def test_get_courses(self, moodle: Moodle):
        courses = moodle.core.course.get_courses()
        assert type(courses) == list
        for co in courses:
            assert isinstance(co, Course)
            assert isinstance(co.id, int)
            assert isinstance(co.shortname, str)
            assert isinstance(co.categoryid, int)
            assert not co.categorysortorder or isinstance(
                co.categorysortorder, int)
            assert isinstance(co.fullname, str)
            assert isinstance(co.displayname, str)
            assert not co.idnumber or isinstance(co.idnumber, str)
            assert isinstance(co.summary, str)
            assert isinstance(co.summaryformat, int)
            assert isinstance(co.format, str)
            assert not co.showgrades or isinstance(co.showgrades, int)
            assert not co.newsitems or isinstance(co.newsitems, int)
            assert isinstance(co.startdate, int)
            assert isinstance(co.enddate, int)
            assert isinstance(co.numsections, int)
            assert not co.maxbytes or isinstance(co.maxbytes, int)
            assert not co.showreports or isinstance(co.showreports, int)
            assert not co.visible or isinstance(co.visible, int)
            assert not co.groupmode or isinstance(co.groupmode, int)
            assert not co.groupmodeforce or isinstance(co.groupmodeforce, int)
            assert not co.defaultgroupingid or isinstance(
                co.defaultgroupingid, int)
            assert not co.enablecompletion or isinstance(
                co.enablecompletion, int)
            assert not co.completionnotify or isinstance(
                co.completionnotify, int)
            assert not co.lang or isinstance(co.lang, str)
            assert not co.forcetheme or isinstance(co.forcetheme, str)

    def test_get_categories(self, moodle: Moodle):
        categories = moodle.core.course.get_categories()
        assert categories is not None
        for category in categories:
            assert isinstance(category, Category)
            assert isinstance(category.id, int)
            assert isinstance(category.name, str)
            assert isinstance(category.description, str)
            assert isinstance(category.descriptionformat, int)
            assert isinstance(category.parent, int)
            assert isinstance(category.sortorder, int)
            assert isinstance(category.coursecount, int)
            assert isinstance(category.depth, int)
            assert isinstance(category.path, str)
            assert not category.idnumber or isinstance(category.idnumber, str)
            assert not category.visible or isinstance(category.visible, int)
            assert not category.visibleold or isinstance(
                category.visibleold, int)
            assert not category.timemodified or isinstance(
                category.timemodified, int)
            assert not category.theme or isinstance(category.theme, str)
