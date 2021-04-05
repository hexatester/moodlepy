from attr import attrib
from typing import List, Optional

from moodle import BaseNameValue
from moodle.attr import dataclass, field


@dataclass
class Restrict:
    """Restrict this content to certain users or courses.
    Constructor arguments:
    params: users (List[int]): List of allowed users.
    params: courses (List[int]): List of allowed courses.
    """
    users: List[int] = attrib(factory=list)
    courses: List[int] = attrib(factory=list)


@dataclass
class File:
    """File in the content.
    Constructor arguments:
    params: filename (Optional[str]): File name.
    params: filepath (Optional[str]): File path.
    params: filesize (Optional[int]): File size.
    params: fileurl (Optional[str]): Downloadable file url.
    params: timemodified (Optional[int]): Time modified.
    params: mimetype (Optional[str]): File mime type.
    params: isexternalfile (Optional[int]): Whether is an external file.
    params: repositorytype (Optional[str]): The repository type for external files.
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
class OtherData(BaseNameValue):
    """Other data that can be used or manipulated by the template via 2-way data-binding.
    Constructor arguments:
    params: name (str): Field name.
    params: value (str): Field value.
    """
    pass


@dataclass
class Template:
    """Template required by the generated content.
    Constructor arguments:
    params: id (str): ID of the template.
    params: html (str): HTML code.
    """
    id: str
    html: str


@dataclass
class Content:
    """A piece of content to be displayed in the Mobile app.
    Constructor arguments:
    params: templates (List[Template]): Templates required by the generated content.
    params: javascript (str): JavaScript code.
    params: otherdata (List[OtherData]): Other data that can be used or manipulated by the template via 2-way data-binding.
    params: files (List[File]): Files in the content.
    params: restrict (List[Restrict]): Restrict this content to certain users or courses.
    """
    javascript: str
    templates: List[Template] = field(factory=list)
    otherdata: List[OtherData] = field(factory=list)
    files: List[File] = field(factory=list)
    restrict: List[Restrict] = field(factory=list)

    @dataclass
    class Args(BaseNameValue):
        """Args for the method are optional.
        Constructor arguments:
        params: name (str): Param name.
        params: value (str): Param value.
        """
        pass
