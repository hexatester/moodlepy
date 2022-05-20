from typing import List, Optional

from moodle import ResponsesFactory, MoodleWarning
from moodle.attr import dataclass, field


@dataclass
class File:
    """File:
    filename (Optional[str]): File name.
    filepath (Optional[str]): File path.
    filesize (Optional[int]): File size.
    fileurl (Optional[str]): Downloadable file url.
    timemodified (Optional[int]): Time modified.
    mimetype (Optional[str]): File mime type.
    isexternalfile (Optional[int]): Whether is an external file.
    repositorytype (Optional[str]): The repository type for external files.
    """

    filename: Optional[str]
    filepath: Optional[str]
    filesize: Optional[int]
    fileurl: Optional[str]
    timemodified: Optional[int]
    mimetype: Optional[str]
    isexternalfile: Optional[int]
    repositorytype: Optional[str]


@dataclass
class Book:
    """Book
    id (int): Book id
    coursemodule (int): Course module id
    course (int): Course id
    name (str): Book name
    intro (str): The Book intro
    introformat (int): intro format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
    introfiles (Optional[List[File]]): Files in the introduction text
    numbering (int): Book numbering configuration
    navstyle (int): Book navigation style configuration
    customtitles (int): Book custom titles type
    revision (Optional[int]): Book revision
    timecreated (Optional[int]): Time of creation
    timemodified (Optional[int]): Time of last modification
    section (Optional[int]): Course section id
    visible (Optional[int]): Visible
    groupmode (Optional[int]): Group mode
    groupingid (Optional[int]): Group id
    """

    id: int
    coursemodule: int
    course: int
    name: str
    intro: str
    introformat: int
    introfiles: Optional[List[File]]
    numbering: int
    navstyle: int
    customtitles: int
    revision: Optional[int]
    timecreated: Optional[int]
    timemodified: Optional[int]
    section: Optional[int]
    visible: Optional[int]
    groupmode: Optional[int]
    groupingid: Optional[int]


@dataclass
class Books(ResponsesFactory[Book]):
    """Books
    Args:
        books (List[Book]): List of course
        warnings (List[MoodleWarning]): List of warnings
    """

    books: List[Book] = field(factory=list)
    warnings: List[MoodleWarning] = field(factory=list)

    @property
    def items(self) -> List[Book]:
        return self.books
