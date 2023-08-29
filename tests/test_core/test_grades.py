from moodle.gradereport.user.gradereport import UserGrade, GradeItem, GradeReport


class TestGrades:
    def test_get_grades(self, moodle, courses):
        grades = moodle.grade_report.user.get_user_grades(course_id=courses[-1].id)
        assert grades is not None
        assert isinstance(grades, GradeReport)
        assert grades.usergrades is not None
        assert type(grades.usergrades) == list
        for user_grade in grades.usergrades:
            assert isinstance(user_grade, UserGrade)
            assert isinstance(user_grade.courseid, int)
            assert isinstance(user_grade.courseidnumber, str)
            assert isinstance(user_grade.gradeitems, list)
            assert isinstance(user_grade.maxdepth, int)
            assert isinstance(user_grade.userfullname, str)
            assert isinstance(user_grade.userid, int)
            assert isinstance(user_grade.useridnumber, str)

            for grade_item in user_grade.gradeitems:
                assert isinstance(grade_item, GradeItem)
                assert not grade_item.categoryid or isinstance(
                    grade_item.categoryid, int
                )
                assert not grade_item.cmid or isinstance(grade_item.cmid, int)
                assert isinstance(grade_item.feedback, str)
                assert isinstance(grade_item.feedbackformat, int)
                assert not grade_item.gradedategraded or isinstance(
                    grade_item.gradedategraded, int
                )
                assert not grade_item.gradedatesubmitted or isinstance(
                    grade_item.gradedatesubmitted, int
                )
                assert isinstance(grade_item.gradeformatted, str)
                assert isinstance(grade_item.gradehiddenbydate, bool)
                assert isinstance(grade_item.gradeishidden, bool)
                assert isinstance(grade_item.gradeislocked, bool)
                assert isinstance(grade_item.gradeisoverridden, bool)
                assert isinstance(grade_item.grademax, int)
                assert isinstance(grade_item.grademin, int)
                assert isinstance(grade_item.gradeneedsupdate, bool)
                assert not grade_item.graderaw or isinstance(grade_item.graderaw, int)
                assert isinstance(grade_item.id, int)
                assert isinstance(grade_item.idnumber, str)
                assert isinstance(grade_item.iteminstance, int)
                assert isinstance(grade_item.itemmodule, str)
                assert isinstance(grade_item.itemname, str)
                assert not grade_item.itemnumber or isinstance(
                    grade_item.itemnumber, int
                )
                assert isinstance(grade_item.itemtype, str)
                assert isinstance(grade_item.locked, bool)
                assert isinstance(grade_item.percentageformatted, str)
                assert isinstance(grade_item.rangeformatted, str)
                assert not grade_item.weightformatted or isinstance(
                    grade_item.weightformatted, str
                )
                assert not grade_item.weightraw or isinstance(grade_item.weightraw, int)
                assert not grade_item.outcomeid or isinstance(grade_item.outcomeid, int)
                assert not grade_item.scaleid or isinstance(grade_item.scaleid, int)

    def test_get_grades_user_filtered(self, moodle, courses):
        grades = moodle.grade_report.user.get_user_grades(
            course_id=courses[-1].id, user_id=47
        )
        assert grades is not None
        assert isinstance(grades, GradeReport)
        assert grades.usergrades is not None
        assert type(grades.usergrades) == list
        assert len(grades.usergrades) == 1
        assert grades.usergrades[0].userid == 47
