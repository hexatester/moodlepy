from typing import List, Optional

from moodle import MoodleWarning, ResponsesFactory
from moodle.attr import dataclass, field


@dataclass
class File:
    """File
    Args:
        filename (Optional[str]): File name.
        filepath (Optional[str]): File path.
        filesize (Optional[int]): File size.
        fileurl (Optional[str]): Downloadable file url.
        timemodified (Optional[int]): Time modified.
        mimetype (Optional[str]): File mime type.
        isexternalfile (Optional[int]): Whether is an external file.
        repositorytype (Optional[str]): The repository type for external files.
    """

    filename: Optional[str] = None
    filepath: Optional[str] = None
    filesize: Optional[int] = None
    fileurl: Optional[str] = None
    timemodified: Optional[int] = None
    mimetype: Optional[str] = None
    isexternalfile: Optional[int] = None
    repositorytype: Optional[str] = None


@dataclass
class Url:
    """Url
    Args:
        id (int): Module id
        coursemodule (int): Course module id
        course (int): Course id
        name (str): URL name
        intro (str): Summary
        introformat (int): Default untuk "1" intro format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
        introfiles (List[File]): Files in the introduction text
        externalurl (str): External URL
        display (int): How to display the url
        displayoptions (str): Display options (width, height)
        parameters (str): Parameters to append to the URL
        timemodified (int): Last time the url was modified
        section (int): Course section id
        visible (int): Module visibility
        groupmode (int): Group mode
        groupingid (int): Grouping id
    """

    id: int
    coursemodule: int
    course: int
    name: str
    intro: str
    introformat: int
    externalurl: str
    display: int
    displayoptions: str
    parameters: str
    timemodified: int
    section: int
    visible: int
    groupmode: int
    groupingid: int
    introfiles: List[File] = field(factory=list)


@dataclass
class Urls(ResponsesFactory[Url]):
    """List of Urls"""

    urls: List[Url] = field(factory=list)
    warnings: List[MoodleWarning] = field(factory=list)
