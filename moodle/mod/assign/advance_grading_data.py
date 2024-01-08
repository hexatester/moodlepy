from typing import List, Optional

from moodle.attr import dataclass, field


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
    levelid: Optional[int] = None
    remark: Optional[str] = None
    remarkformat: Optional[int] = None
    enrichedbenchmark: Optional[float] = None
    enrichedbenchmarkstudent: Optional[float] = None
    enrichedbenchmarkstudents: Optional[float] = None


@dataclass
class Criterion:
    """Criterion
    Args:
        criterionid (int): criterion id
        fillings (List[Filling]): filling
    """

    criterionid: int
    fillings: List[Filling] = field(factory=list)


@dataclass
class Rubric:
    """Rubric
    Args:
        criteria (List[Criterion]): list of criterion
    """

    criteria: List[Criterion] = field(factory=list)


@dataclass
class AdvanceGradingData:
    """Advance Grading Data
    Args:
        erubric (Optional[Rubric]): list of Rubric
        guide (Optional[Rubric]): list of Rubric
        rubric (Optional[Rubric]): list of Rubric
    """

    erubric: Optional[Rubric] = None
    guide: Optional[Rubric] = None
    rubric: Optional[Rubric] = None
