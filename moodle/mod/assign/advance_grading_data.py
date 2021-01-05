from moodle.attr import dataclass
from typing import List, Optional


@dataclass
class Filling:
    """Filling
    Args:
        criterionid (int): criterion id
        levelid (Optional[int]): level id
        remark (Optional[str]): remark
        remarkformat (Optional[int]): remark format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
        enrichedbenchmark (Optional[float]): enrichedbenchmark
        enrichedbenchmarkstudent (Optional[float]): enrichedbenchmarkstudent
        enrichedbenchmarkstudents (Optional[float]): enrichedbenchmarkstudents
    """
    criterionid: int
    levelid: Optional[int]
    remark: Optional[str]
    remarkformat: Optional[int]
    enrichedbenchmark: Optional[float]
    enrichedbenchmarkstudent: Optional[float]
    enrichedbenchmarkstudents: Optional[float]


@dataclass
class Criterion:
    """Criterion
    Args:
        criterionid (int): criterion id
        fillings (List[Filling]): filling
    """
    criterionid: int
    fillings: List[Filling]


@dataclass
class Rubric:
    """Rubric
    Args:
        criteria (List[Criterion]): list of criterion
    """
    criteria: List[Criterion]


@dataclass
class AdvanceGradingData:
    """Advance Grading Data
    Args:
        erubric (Optional[Rubric]): list of Rubric
        guide (Optional[Rubric]): list of Rubric
        rubric (Optional[Rubric]): list of Rubric
    """
    erubric: Optional[Rubric]
    guide: Optional[Rubric]
    rubric: Optional[Rubric]
