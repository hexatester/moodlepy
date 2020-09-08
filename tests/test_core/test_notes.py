from moodle.core.notes import SiteNote, CourseNote, PersonalNote, CourseNotes, ViewNotes


class TestNotes:
    # TODO Test for core_notes
    def test_create_notes(self, moodle, user_id):
        pass

    def test_get_course_notes(self, moodle, courses):
        for course in courses:
            course_notes = moodle.core.notes.get_course_notes(course.id)
            assert isinstance(course_notes, CourseNotes)
            for site_note in course_notes.sitenotes:
                assert isinstance(site_note, SiteNote)
            for course_note in course_notes.coursenotes:
                assert isinstance(course_note, CourseNote)
            for personal_note in course_notes.personalnotes:
                assert isinstance(personal_note, PersonalNote)

    def test_view_notes(self, moodle, courses, user_id):
        for course in courses:
            view_notes = moodle.core.notes.view_notes(course.id, user_id)
            assert isinstance(view_notes, ViewNotes)
            assert type(view_notes.status) == bool

    def test_delete_notes(self, moodle):
        pass
