from moodle import BaseMoodle


class BaseCompetency(BaseMoodle):
    def add_competency_to_course(self, **kwargs):
        data = self.moodle.get("core_competency_add_competency_to_course", **kwargs)
        return data

    def add_competency_to_plan(self, **kwargs):
        data = self.moodle.get("core_competency_add_competency_to_plan", **kwargs)
        return data

    def add_competency_to_template(self, **kwargs):
        data = self.moodle.get("core_competency_add_competency_to_template", **kwargs)
        return data

    def add_related_competency(self, **kwargs):
        data = self.moodle.get("core_competency_add_related_competency", **kwargs)
        return data

    def approve_plan(self, **kwargs):
        data = self.moodle.get("core_competency_approve_plan", **kwargs)
        return data

    def competency_framework_viewed(self, **kwargs):
        data = self.moodle.get("core_competency_competency_framework_viewed", **kwargs)
        return data

    def competency_viewed(self, **kwargs):
        data = self.moodle.get("core_competency_competency_viewed", **kwargs)
        return data

    def complete_plan(self, **kwargs):
        data = self.moodle.get("core_competency_complete_plan", **kwargs)
        return data

    def count_competencies(self, **kwargs):
        data = self.moodle.get("core_competency_count_competencies", **kwargs)
        return data

    def count_competencies_in_course(self, **kwargs):
        data = self.moodle.get("core_competency_count_competencies_in_course", **kwargs)
        return data

    def count_competencies_in_template(self, **kwargs):
        data = self.moodle.get(
            "core_competency_count_competencies_in_template", **kwargs
        )
        return data

    def count_competency_frameworks(self, **kwargs):
        data = self.moodle.get("core_competency_count_competency_frameworks", **kwargs)
        return data

    def count_course_module_competencies(self, **kwargs):
        data = self.moodle.get(
            "core_competency_count_course_module_competencies", **kwargs
        )
        return data

    def count_courses_using_competency(self, **kwargs):
        data = self.moodle.get(
            "core_competency_count_courses_using_competency", **kwargs
        )
        return data

    def count_templates(self, **kwargs):
        data = self.moodle.get("core_competency_count_templates", **kwargs)
        return data

    def count_templates_using_competency(self, **kwargs):
        data = self.moodle.get(
            "core_competency_count_templates_using_competency", **kwargs
        )
        return data

    def create_competency(self, **kwargs):
        data = self.moodle.get("core_competency_create_competency", **kwargs)
        return data

    def create_competency_framework(self, **kwargs):
        data = self.moodle.get("core_competency_create_competency_framework", **kwargs)
        return data

    def create_plan(self, **kwargs):
        data = self.moodle.get("core_competency_create_plan", **kwargs)
        return data

    def create_template(self, **kwargs):
        data = self.moodle.get("core_competency_create_template", **kwargs)
        return data

    def create_user_evidence_competency(self, **kwargs):
        data = self.moodle.get(
            "core_competency_create_user_evidence_competency", **kwargs
        )
        return data

    def delete_competency(self, **kwargs):
        data = self.moodle.get("core_competency_delete_competency", **kwargs)
        return data

    def delete_competency_framework(self, **kwargs):
        data = self.moodle.get("core_competency_delete_competency_framework", **kwargs)
        return data

    def delete_evidence(self, **kwargs):
        data = self.moodle.get("core_competency_delete_evidence", **kwargs)
        return data

    def delete_plan(self, **kwargs):
        data = self.moodle.get("core_competency_delete_plan", **kwargs)
        return data

    def delete_template(self, **kwargs):
        data = self.moodle.get("core_competency_delete_template", **kwargs)
        return data

    def delete_user_evidence(self, **kwargs):
        data = self.moodle.get("core_competency_delete_user_evidence", **kwargs)
        return data

    def delete_user_evidence_competency(self, **kwargs):
        data = self.moodle.get(
            "core_competency_delete_user_evidence_competency", **kwargs
        )
        return data

    def duplicate_competency_framework(self, **kwargs):
        data = self.moodle.get(
            "core_competency_duplicate_competency_framework", **kwargs
        )
        return data

    def duplicate_template(self, **kwargs):
        data = self.moodle.get("core_competency_duplicate_template", **kwargs)
        return data

    def get_scale_values(self, **kwargs):
        data = self.moodle.get("core_competency_get_scale_values", **kwargs)
        return data

    def grade_competency(self, **kwargs):
        data = self.moodle.get("core_competency_grade_competency", **kwargs)
        return data

    def grade_competency_in_course(self, **kwargs):
        data = self.moodle.get("core_competency_grade_competency_in_course", **kwargs)
        return data

    def grade_competency_in_plan(self, **kwargs):
        data = self.moodle.get("core_competency_grade_competency_in_plan", **kwargs)
        return data

    def list_competencies(self, **kwargs):
        data = self.moodle.get("core_competency_list_competencies", **kwargs)
        return data

    def list_competencies_in_template(self, **kwargs):
        data = self.moodle.get(
            "core_competency_list_competencies_in_template", **kwargs
        )
        return data

    def list_competency_frameworks(self, **kwargs):
        data = self.moodle.get("core_competency_list_competency_frameworks", **kwargs)
        return data

    def list_course_competencies(self, **kwargs):
        data = self.moodle.get("core_competency_list_course_competencies", **kwargs)
        return data

    def list_course_module_competencies(self, **kwargs):
        data = self.moodle.get(
            "core_competency_list_course_module_competencies", **kwargs
        )
        return data

    def list_plan_competencies(self, **kwargs):
        data = self.moodle.get("core_competency_list_plan_competencies", **kwargs)
        return data

    def list_templates(self, **kwargs):
        data = self.moodle.get("core_competency_list_templates", **kwargs)
        return data

    def list_templates_using_competency(self, **kwargs):
        data = self.moodle.get(
            "core_competency_list_templates_using_competency", **kwargs
        )
        return data

    def list_user_plans(self, **kwargs):
        data = self.moodle.get("core_competency_list_user_plans", **kwargs)
        return data

    def move_down_competency(self, **kwargs):
        data = self.moodle.get("core_competency_move_down_competency", **kwargs)
        return data

    def move_up_competency(self, **kwargs):
        data = self.moodle.get("core_competency_move_up_competency", **kwargs)
        return data

    def plan_cancel_review_request(self, **kwargs):
        data = self.moodle.get("core_competency_plan_cancel_review_request", **kwargs)
        return data

    def plan_request_review(self, **kwargs):
        data = self.moodle.get("core_competency_plan_request_review", **kwargs)
        return data

    def plan_start_review(self, **kwargs):
        data = self.moodle.get("core_competency_plan_start_review", **kwargs)
        return data

    def plan_stop_review(self, **kwargs):
        data = self.moodle.get("core_competency_plan_stop_review", **kwargs)
        return data

    def read_competency(self, **kwargs):
        data = self.moodle.get("core_competency_read_competency", **kwargs)
        return data

    def read_competency_framework(self, **kwargs):
        data = self.moodle.get("core_competency_read_competency_framework", **kwargs)
        return data

    def read_plan(self, **kwargs):
        data = self.moodle.get("core_competency_read_plan", **kwargs)
        return data

    def read_template(self, **kwargs):
        data = self.moodle.get("core_competency_read_template", **kwargs)
        return data

    def read_user_evidence(self, **kwargs):
        data = self.moodle.get("core_competency_read_user_evidence", **kwargs)
        return data

    def remove_competency_from_course(self, **kwargs):
        data = self.moodle.get(
            "core_competency_remove_competency_from_course", **kwargs
        )
        return data

    def remove_competency_from_plan(self, **kwargs):
        data = self.moodle.get("core_competency_remove_competency_from_plan", **kwargs)
        return data

    def remove_competency_from_template(self, **kwargs):
        data = self.moodle.get(
            "core_competency_remove_competency_from_template", **kwargs
        )
        return data

    def remove_related_competency(self, **kwargs):
        data = self.moodle.get("core_competency_remove_related_competency", **kwargs)
        return data

    def reopen_plan(self, **kwargs):
        data = self.moodle.get("core_competency_reopen_plan", **kwargs)
        return data

    def reorder_course_competency(self, **kwargs):
        data = self.moodle.get("core_competency_reorder_course_competency", **kwargs)
        return data

    def reorder_plan_competency(self, **kwargs):
        data = self.moodle.get("core_competency_reorder_plan_competency", **kwargs)
        return data

    def reorder_template_competency(self, **kwargs):
        data = self.moodle.get("core_competency_reorder_template_competency", **kwargs)
        return data

    def request_review_of_user_evidence_linked_competencies(self, **kwargs):
        data = self.moodle.get(
            "core_competency_request_review_of_user_evidence_linked_competencies",  # NOQA
            **kwargs
        )
        return data

    def search_competencies(self, **kwargs):
        data = self.moodle.get("core_competency_search_competencies", **kwargs)
        return data

    def set_course_competency_ruleoutcome(self, **kwargs):
        data = self.moodle.get(
            "core_competency_set_course_competency_ruleoutcome", **kwargs
        )
        return data

    def set_parent_competency(self, **kwargs):
        data = self.moodle.get("core_competency_set_parent_competency", **kwargs)
        return data

    def template_has_related_data(self, **kwargs):
        data = self.moodle.get("core_competency_template_has_related_data", **kwargs)
        return data

    def template_viewed(self, **kwargs):
        data = self.moodle.get("core_competency_template_viewed", **kwargs)
        return data

    def unapprove_plan(self, **kwargs):
        data = self.moodle.get("core_competency_unapprove_plan", **kwargs)
        return data

    def unlink_plan_from_template(self, **kwargs):
        data = self.moodle.get("core_competency_unlink_plan_from_template", **kwargs)
        return data

    def update_competency(self, **kwargs):
        data = self.moodle.get("core_competency_update_competency", **kwargs)
        return data

    def update_competency_framework(self, **kwargs):
        data = self.moodle.get("core_competency_update_competency_framework", **kwargs)
        return data

    def update_course_competency_settings(self, **kwargs):
        data = self.moodle.get(
            "core_competency_update_course_competency_settings", **kwargs
        )
        return data

    def update_plan(self, **kwargs):
        data = self.moodle.get("core_competency_update_plan", **kwargs)
        return data

    def update_template(self, **kwargs):
        data = self.moodle.get("core_competency_update_template", **kwargs)
        return data

    def user_competency_cancel_review_request(self, **kwargs):
        data = self.moodle.get(
            "core_competency_user_competency_cancel_review_request", **kwargs
        )
        return data

    def user_competency_plan_viewed(self, **kwargs):
        data = self.moodle.get("core_competency_user_competency_plan_viewed", **kwargs)
        return data

    def user_competency_request_review(self, **kwargs):
        data = self.moodle.get(
            "core_competency_user_competency_request_review", **kwargs
        )
        return data

    def user_competency_start_review(self, **kwargs):
        data = self.moodle.get("core_competency_user_competency_start_review", **kwargs)
        return data

    def user_competency_stop_review(self, **kwargs):
        data = self.moodle.get("core_competency_user_competency_stop_review", **kwargs)
        return data

    def user_competency_viewed(self, **kwargs):
        data = self.moodle.get("core_competency_user_competency_viewed", **kwargs)
        return data

    def user_competency_viewed_in_course(self, **kwargs):
        data = self.moodle.get(
            "core_competency_user_competency_viewed_in_course", **kwargs
        )
        return data

    def user_competency_viewed_in_plan(self, **kwargs):
        data = self.moodle.get(
            "core_competency_user_competency_viewed_in_plan", **kwargs
        )
        return data
