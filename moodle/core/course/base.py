from dacite import from_dict
from typing import List
from moodle import BaseMoodle
from . import CourseCategory


class BaseCourse(BaseMoodle):
    def get_categories(self) -> List[CourseCategory]:
        datas = self.moodle.get('core_course_get_categories')
        results: List[CourseCategory] = []
        if datas:
            for data in datas:
                results.append(from_dict(CourseCategory, data))
        return results
