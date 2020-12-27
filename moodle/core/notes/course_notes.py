from dataclasses import dataclass
from typing import List, Optional
from moodle import MoodleWarning, ResponsesFactory
from . import SiteNote, CourseNote, PersonalNote


@dataclass
class CourseNotes(ResponsesFactory[CourseNote]):
    """Course Notes
    Constructor arguments:
    params: sitenotes (List[SiteNote]): site notes
    params: coursenotes (List[CourseNote]): couse notes
    params: personalnotes (List[PersonalNote]): personal notes
    params: canmanagesystemnotes (Optional[int]): Whether the user can manage notes at system level.
    params: canmanagecoursenote (Optional[int]): Whether the user can manage notes at the given course.
    params: warnings (List[Warning]): list of warnings
    """
    sitenotes: List[SiteNote]
    coursenotes: List[CourseNote]
    personalnotes: List[PersonalNote]
    canmanagesystemnotes: Optional[int]
    canmanagecoursenote: Optional[int]
    warnings: List[MoodleWarning]

    @property
    def items(self) -> List[CourseNote]:
        return self.coursenotes
