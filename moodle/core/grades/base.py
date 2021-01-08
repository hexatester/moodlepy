from typing import List, Optional

from moodle import BaseMoodle
from . import Grades


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

    def get_grades(self,
                   courseid: int,
                   component: int = None,
                   activityid: int = None,
                   userids: List[int] = None) -> Grades:
        """**DEPRECATED** Please do not call this function any more. Returns student course total grade and grades for activities. This function does not return category or manual items. This function is suitable for managers or teachers not students.

        Args:
            courseid (int): id of course
            component (int, optional): A component, for example mod_forum or mod_quiz. Defaults to None.
            activityid (int, optional): The activity ID. Defaults to None.
            userids (List[int], optional): An array of user IDs, leave empty to just retrieve grade item information. Defaults to None.

        Returns:
            Grades: Student course total grade and grades for activities.
        """
        data = self.moodle.post(
            'core_grades_get_grades',
            component=component or '',
            activityid=activityid,
            userids=userids or list(),
        )
        return self._tr(Grades, data)

    def grader_gradingpanel_point_fetch(
        self,
        component: str,
        contextid: int,
        itemname: str,
        gradeduserid: int,
    ) -> dict:
        """Fetch the data required to display the grader grading panel for simple grading, creating the grade item if required

        Args:
            component (str): The name of the component
            contextid (int): The ID of the context being graded
            itemname (str): The grade item itemname being graded
            gradeduserid (int): The ID of the user show

        Returns:
            dict: gradingpanel
        """
        data = self.moodle.post(
            'core_grades_grader_gradingpanel_point_fetch',
            component=component,
            contextid=contextid,
            itemname=itemname,
            gradeduserid=gradeduserid,
        )
        # TODO : Add type for data!
        return data

    def grader_gradingpanel_point_store(
        self,
        component: str,
        contextid: int,
        itemname: str,
        gradeduserid: int,
        formdata: str,
        notifyuser: int = None,
    ) -> dict:
        """Store the data required to display the grader grading panel for simple grading

        Args:
            component (str): The name of the component
            contextid (int): The ID of the context being graded
            itemname (str): The grade item itemname being graded
            gradeduserid (int): The ID of the user show
            formdata (str): The serialised form data representing the grade
            notifyuser (int, optional): Wheteher to notify the user or not. Defaults to None.

        Returns:
            dict: gradingpanel
        """
        data = self.moodle.post(
            'core_grades_grader_gradingpanel_point_store',
            component=component,
            contextid=contextid,
            itemname=itemname,
            gradeduserid=gradeduserid,
            notifyuser=notifyuser or '',
            formdata=formdata,
        )
        # TODO : Add type for data!
        return data

    def grader_gradingpanel_scale_fetch(
        self,
        component: str,
        contextid: int,
        itemname: str,
        gradeduserid: int,
    ) -> dict:
        """Fetch the data required to display the grader grading panel for scale-based grading, creating the grade item if required

        Args:
            component (str): The name of the component
            contextid (int): The ID of the context being graded
            itemname (str): The grade item itemname being graded
            gradeduserid (int): The ID of the user show

        Returns:
            dict: gradingpanel scale
        """
        data = self.moodle.post(
            'core_grades_grader_gradingpanel_scale_fetch',
            component=component,
            contextid=contextid,
            itemname=itemname,
            gradeduserid=gradeduserid,
        )
        # TODO : Add type for data!
        return data

    def grader_gradingpanel_scale_store(self):
        data = self.moodle.post('core_grades_grader_gradingpanel_scale_store')
        return data

    def update_grades(
        self,
        source: str,
        courseid: int,
        component: str,
        activityid: int,
        itemnumber: int,
        grades: List[dict],
        itemname: Optional[str] = None,
        idnumber: Optional[int] = None,
        gradetype: Optional[int] = None,
        grademax: Optional[float] = None,
        grademin: Optional[float] = None,
        scaleid: Optional[int] = None,
        multfactor: Optional[float] = None,
        plusfactor: Optional[float] = None,
        deleted: Optional[int] = None,
        hidden: Optional[int] = None,
    ) -> int:
        """Update a grade item and associated student grades.

        Args:
            source (str): The source of the grade update
            courseid (int): id of course
            component (str): A component, for example mod_forum or mod_quiz
            activityid (int): The activity ID
            itemnumber (int): grade item ID number for modules that have multiple grades. Typically this is 0.
            grades (List[dict]): Any student grades to alter. list of {studentid:int, grade:float, str_feedback: Optional[str]}
            itemname (Optional[str], optional): The grade item name. Defaults to None.
            idnumber (Optional[int], optional): Arbitrary ID provided by the module responsible for the grade item. Defaults to None.
            gradetype (Optional[int], optional): The type of grade (0 = none, 1 = value, 2 = scale, 3 = text). Defaults to None.
            grademax (Optional[float], optional): Maximum grade allowed. Defaults to None.
            grademin (Optional[float], optional): Minimum grade allowed. Defaults to None.
            scaleid (Optional[int], optional): The ID of the custom scale being is used. Defaults to None.
            multfactor (Optional[float], optional): Multiply all grades by this number. Defaults to None.
            plusfactor (Optional[float], optional): Add this to all grades. Defaults to None.
            deleted (Optional[int], optional): True if the grade item should be deleted. Defaults to None.
            hidden (Optional[int], optional): True if the grade item is hidden. Defaults to None.

        Returns:
            int: A value like 0 => OK, 1 => FAILED as defined in lib/grade/constants.php
        """
        itemdetails = dict(
            itemname=itemname,
            idnumber=idnumber,
            gradetype=gradetype,
            grademax=grademax,
            grademin=grademin,
            scaleid=scaleid,
            multfactor=multfactor,
            plusfactor=plusfactor,
            deleted=deleted,
            hidden=hidden,
        )
        data = self.moodle.post(
            'core_grades_update_grades',
            source=source,
            courseid=courseid,
            component=component,
            activityid=activityid,
            itemnumber=itemnumber,
            grades=grades,
            itemdetails=itemdetails,
        )
        return data
