from typing import List

from moodle import BaseMoodle
from moodle.base.general import GeneralNameValue


class BaseWorkshop(BaseMoodle):
    def add_submission(
        self,
        workshopid: int,
        title: str,
        content: str = "",
        contentformat: int = 0,
        inlineattachmentsid: int = 0,
        attachmentsid: int = 0,
    ):
        data = self.moodle.post(
            "mod_workshop_add_submission",
            workshopid=workshopid,
            title=title,
            content=content,
            contentformat=contentformat,
            inlineattachmentsid=inlineattachmentsid,
            attachmentsid=attachmentsid,
        )
        return data

    def delete_submission(self, submissionid: int):
        data = self.moodle.post(
            "mod_workshop_delete_submission",
            submissionid=submissionid,
        )
        return data

    def evaluate_assessment(
        self,
        assessmentid: int,
        feedbacktext: str = "",
        feedbackformat: int = 0,
        weight: int = 1,
        gradinggradeover: str = "",
    ):
        data = self.moodle.post(
            "mod_workshop_evaluate_assessment",
            assessmentid=assessmentid,
            feedbacktext=feedbacktext,
            feedbackformat=feedbackformat,
            weight=weight,
            gradinggradeover=gradinggradeover,
        )
        return data

    def evaluate_submission(
        self,
        submissionid: int,
        feedbacktext: str = "",
        feedbackformat: int = 0,
        published: int = None,
        gradeover: str = "",
    ):
        data = self.moodle.post(
            "mod_workshop_evaluate_submission",
            submissionid=submissionid,
            feedbacktext=feedbacktext,
            feedbackformat=feedbackformat,
            published=published or "",
            gradeover=gradeover,
        )
        return data

    def get_assessment(self, assessmentid: int):
        data = self.moodle.post(
            "mod_workshop_get_assessment",
            assessmentid=assessmentid,
        )
        return data

    def get_assessment_form_definition(
        self, assessmentid: int, mode: str = "assessment"
    ):
        data = self.moodle.post(
            "mod_workshop_get_assessment_form_definition",
            assessmentid=assessmentid,
            mode=mode,
        )
        return data

    def get_grades(self, workshopid: int, userid: int = 0):
        data = self.moodle.post(
            "mod_workshop_get_grades",
            workshopid=workshopid,
            userid=userid,
        )
        return data

    def get_grades_report(
        self,
        workshopid: int,
        groupid: int = 0,
        sortby: str = "lastname",
        sortdirection: str = "ASC",
        page: int = 0,
        perpage: int = 0,
    ):
        data = self.moodle.post(
            "mod_workshop_get_grades_report",
            workshopid=workshopid,
            groupid=groupid,
            sortby=sortby,
            sortdirection=sortdirection,
            page=page,
            perpage=perpage,
        )
        return data

    def get_reviewer_assessments(self, workshopid: int, userid: int = 0):
        data = self.moodle.post(
            "mod_workshop_get_reviewer_assessments",
            workshopid=workshopid,
            userid=userid,
        )
        return data

    def get_submission(self, submissionid: int):
        data = self.moodle.post(
            "mod_workshop_get_submission",
            submissionid=submissionid,
        )
        return data

    def get_submission_assessments(self, submissionid: int):
        data = self.moodle.post(
            "mod_workshop_get_submission_assessments",
            submissionid=submissionid,
        )
        return data

    def get_submissions(
        self,
        workshopid: int,
        userid: int = 0,
        groupid: int = 0,
        page: int = 0,
        perpage: int = 0,
    ):
        data = self.moodle.post(
            "mod_workshop_get_submissions",
            workshopid=workshopid,
            userid=userid,
            groupid=groupid,
            page=page,
            perpage=perpage,
        )
        return data

    def get_user_plan(self, workshopid: int, userid: int = 0):
        data = self.moodle.post(
            "mod_workshop_get_user_plan",
            workshopid=workshopid,
            userid=userid,
        )
        return data

    def get_workshop_access_information(self, workshopid: int):
        data = self.moodle.post(
            "mod_workshop_get_workshop_access_information",
            workshopid=workshopid,
        )
        return data

    def get_workshops_by_courses(self, courseids: List[int]):
        data = self.moodle.post(
            "mod_workshop_get_workshops_by_courses",
            courseids=courseids,
        )
        return data

    def update_assessment(self, assessmentid: int, data: List[GeneralNameValue]):
        data = self.moodle.post(
            "mod_workshop_update_assessment",
            assessmentid=assessmentid,
            data=data,
        )
        return data

    def update_submission(
        self,
        submissionid: int,
        title: str,
        content: str = "",
        contentformat: int = 0,
        inlineattachmentsid: int = 0,
        attachmentsid: int = 0,
    ):
        data = self.moodle.post(
            "mod_workshop_update_submission",
            submissionid=submissionid,
            title=title,
            content=content,
            contentformat=contentformat,
            inlineattachmentsid=inlineattachmentsid,
            attachmentsid=attachmentsid,
        )
        return data

    def view_submission(self, submissionid: int):
        data = self.moodle.post(
            "mod_workshop_view_submission",
            submissionid=submissionid,
        )
        return data

    def view_workshop(self, workshopid: int):
        data = self.moodle.post(
            "mod_workshop_view_workshop",
            workshopid=workshopid,
        )
        return data
