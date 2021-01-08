from moodle import BaseMoodle


class BaseGrades(BaseMoodle):
    def create_gradecategory(self):
        data = self.moodle.post('core_grades_create_gradecategory')
        return data

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
