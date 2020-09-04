from moodle import BaseMoodle


class BaseCohort(BaseMoodle):
    def add_cohort_members(self):
        data = self.moodle.get('core_cohort_add_cohort_members')
        return data

    def create_cohorts(self):
        data = self.moodle.get('core_cohort_create_cohorts')
        return data

    def delete_cohort_members(self):
        data = self.moodle.get('core_cohort_delete_cohort_members')
        return data

    def delete_cohorts(self):
        data = self.moodle.get('core_cohort_delete_cohorts')
        return data

    def get_cohort_members(self):
        data = self.moodle.get('core_cohort_get_cohort_members')
        return data

    def get_cohorts(self):
        data = self.moodle.get('core_cohort_get_cohorts')
        return data

    def search_cohorts(self):
        data = self.moodle.get('core_cohort_search_cohorts')
        return data

    def update_cohorts(self):
        data = self.moodle.get('core_cohort_update_cohorts')
        return data
