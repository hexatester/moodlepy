from dacite import from_dict
from typing import List
from moodlepy import BaseMoodle, CourseCategory


class BaseCourse(BaseMoodle):
    @property
    def get_categories(self) -> List[CourseCategory]:
        datas = self.moodle.get('core_course_get_categories')
        results: List[CourseCategory] = []
        if datas:
            for data in datas:
                results.append(from_dict(CourseCategory, data))
        return results
