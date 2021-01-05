from attr import attrib
from typing import List, Optional

from moodle import MoodleWarning, ResponsesFactory
from moodle.attr import dataclass, fields


@dataclass
class Page:
    """Page
    Args:
        id (int): The id of this lesson page
        lessonid (int): The id of the lesson this page belongs to
        prevpageid (int): The id of the page before this one
        nextpageid (int): The id of the next page in the page sequence
        qtype (int): Identifies the page type of this page
        qoption (int): Used to record page type specific options
        layout (int): Used to record page specific layout selections
        display (int): Used to record page specific display selections
        timecreated (int): Timestamp for when the page was created
        timemodified (int): Timestamp for when the page was last modified
        title (Optional[str]): The title of this page
        contents (Optional[str]): The contents of this page
        contentsformat (Optional[int]): contents format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
        displayinmenublock (int): Toggles display in the left menu block
        type (int): The type of the page [question | structure]
        typeid (int): The unique identifier for the page type
        typestring (str): The string that describes this page type
    """
    id: int
    lessonid: int
    prevpageid: int
    nextpageid: int
    qtype: int
    qoption: int
    layout: int
    display: int
    timecreated: int
    timemodified: int
    title: Optional[str]
    contents: Optional[str]
    contentsformat: Optional[int]
    displayinmenublock: int
    type: int
    typeid: int
    typestring: str


@dataclass
class LessonPage:
    """Lesson Page
    Args:
        page (Page): Page fields
        filescount (int): The total number of files attached to the page
        filessizetotal (int): The total size of the files
        answerids (List[int]): List of answers ids (empty for content pages in  Moodle 1.9)
        jumps (List[int]): List of possible page jumps
    """
    page: Page
    filescount: int
    filessizetotal: int
    answerids: List[int] = attrib(factory=list)
    jumps: List[int] = attrib(factory=list)


@dataclass
class Pages(ResponsesFactory[LessonPage]):
    """Pages
    Args:
        pages (List[LessonPage]): LessonPage fields
        warnings (List[Warning]): list of warnings
    """
    pages: List[LessonPage] = fields(LessonPage)
    warnings: List[MoodleWarning] = fields(MoodleWarning)
