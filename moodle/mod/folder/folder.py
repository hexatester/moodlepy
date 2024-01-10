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
class Folder:
    """Folder
    Args:
        id (int): Module id
        coursemodule (int): Course module id
        course (int): Course id
        name (str): Page name
        intro (str): Summary
        introformat (int): Default untuk "1" intro format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
        introfiles (List[File]): Files in the introduction text
        revision (int): Incremented when after each file changes, to avoid cache
        timemodified (int): Last time the folder was modified
        display (int): Display type of folder contents on a separate page or inline
        showexpanded (int): 1 = expanded, 0 = collapsed for sub-folders
        showdownloadfolder (int): Whether to show the download folder button
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
    revision: int
    timemodified: int
    display: int
    showexpanded: int
    showdownloadfolder: int
    section: int
    visible: int
    groupmode: int
    groupingid: int
    introfiles: List[File] = field(factory=list)


@dataclass
class Folders(ResponsesFactory[Folder]):
    """Folders (list of Folder)
    Args:
        folders (List[Folder]): list of folders
        warnings (List[Warning]): list of warnings
    """

    folders: List[Folder] = field(factory=list)
    warnings: List[MoodleWarning] = field(factory=list)

    @property
    def items(self) -> List[Folder]:
        return self.folders
