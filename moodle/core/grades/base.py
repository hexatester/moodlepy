from typing import Optional

from moodle import BaseMoodle


class BaseGrades(BaseMoodle):
    def create_gradecategory(
        self,
        courseid: int,
        fullname: str,
        aggregation: Optional[int] = None,
        aggregateonlygraded: Optional[int] = None,
        aggregateoutcomes: Optional[int] = None,
        droplow: Optional[int] = None,
        itemname: Optional[str] = None,
        iteminfo: Optional[str] = None,
        idnumber: Optional[str] = None,
        gradetype: Optional[int] = None,
        grademax: Optional[int] = None,
        grademin: Optional[int] = None,
        gradepass: Optional[int] = None,
        display: Optional[int] = None,
        decimals: Optional[int] = None,
        hiddenuntil: Optional[int] = None,
        locktime: Optional[int] = None,
        weightoverride: Optional[int] = None,
        aggregationcoef2: Optional[str] = None,
        parentcategoryid: Optional[int] = None,
        parentcategoryidnumber: Optional[str] = None,
    ) -> Optional[int]:
        """Create a grade category inside a course gradebook.

        Args:
            courseid (int): id of course
            fullname (str): fullname of category
            aggregation (Optional[int], optional): aggregation method. Defaults to None.
            aggregateonlygraded (Optional[int], optional): exclude empty grades. Defaults to None.
            aggregateoutcomes (Optional[int], optional): aggregate outcomes. Defaults to None.
            droplow (Optional[int], optional): drop low grades. Defaults to None.
            itemname (Optional[str], optional): the category total name. Defaults to None.
            iteminfo (Optional[str], optional): the category iteminfo. Defaults to None.
            idnumber (Optional[str], optional): the category idnumber. Defaults to None.
            gradetype (Optional[int], optional): the grade type. Defaults to None.
            grademax (Optional[int], optional): the grade max. Defaults to None.
            grademin (Optional[int], optional): the grade min. Defaults to None.
            gradepass (Optional[int], optional): the grade to pass. Defaults to None.
            display (Optional[int], optional): the display type. Defaults to None.
            decimals (Optional[int], optional): the decimal count. Defaults to None.
            hiddenuntil (Optional[int], optional): grades hidden until. Defaults to None.
            locktime (Optional[int], optional): lock grades after. Defaults to None.
            weightoverride (Optional[int], optional): weight adjusted. Defaults to None.
            aggregationcoef2 (Optional[str], optional): weight coefficient. Defaults to None.
            parentcategoryid (Optional[int], optional): The parent category id. Defaults to None.
            parentcategoryidnumber (Optional[str], optional): the parent category idnumber. Defaults to None.

        Returns:
            Optional[int]: The ID of the created category
        """
        options = dict(
            aggregation=aggregation,
            aggregateonlygraded=aggregateonlygraded,
            aggregateoutcomes=aggregateoutcomes,
            droplow=droplow,
            itemname=itemname,
            iteminfo=iteminfo,
            idnumber=idnumber,
            gradetype=gradetype,
            grademax=grademax,
            grademin=grademin,
            gradepass=gradepass,
            display=display,
            decimals=decimals,
            hiddenuntil=hiddenuntil,
            locktime=locktime,
            weightoverride=weightoverride,
            aggregationcoef2=aggregationcoef2,
            parentcategoryid=parentcategoryid,
            parentcategoryidnumber=parentcategoryidnumber,
        )
        data = self.moodle.post(
            'core_grades_create_gradecategory',
            courseid=courseid,
            fullname=fullname,
            options=options,
        )
        return dict(data).get('categoryid')

    def get_grades(self):
        data = self.moodle.post('core_grades_get_grades')
        return data

    def grader_gradingpanel_point_fetch(self):
        data = self.moodle.post('core_grades_grader_gradingpanel_point_fetch')
        return data

    def grader_gradingpanel_point_store(self):
        data = self.moodle.post('core_grades_grader_gradingpanel_point_store')
        return data

    def grader_gradingpanel_scale_fetch(self):
        data = self.moodle.post('core_grades_grader_gradingpanel_scale_fetch')
        return data

    def grader_gradingpanel_scale_store(self):
        data = self.moodle.post('core_grades_grader_gradingpanel_scale_store')
        return data

    def update_grades(self):
        data = self.moodle.post('core_grades_update_grades')
        return data
