from typing import List, Optional

from moodle import MoodleWarning, ResponsesFactory
from moodle.attr import dataclass, field


@dataclass
class BlockFile:
    """Block file
    Constructor arguments:
    param: filename (Optional[str]): File name.
    param: filepath (Optional[str]): File path.
    param: filesize (Optional[int]): File size.
    param: fileurl (Optional[str]): Downloadable file url.
    param: timemodified (Optional[int]): Time modified.
    param: mimetype (Optional[str]): File mime type.
    param: isexternalfile (Optional[int]): Whether is an external file.
    param: repositorytype (Optional[str]): The repository type for external files
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
class BlockContent:
    """Block content
    Constructor arguments:
    param: title (str) : Block title.
    param: content (str) : Block contents.
    param: contentformat (int) : content format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
    param: footer (str) : Block footer.
    param: files (List[BlockFile]) : Block files.
    """

    title: str
    content: str
    contentformat: int
    footer: Optional[str] = None
    files: List[BlockFile] = field(factory=list)

    def __str__(self) -> str:
        return self.title


@dataclass
class Block:
    """Block information
    Constructor arguments:
    params: instanceid (int): Block instance id.
    params: name (str): Block name.
    params: region (str): Block region.
    params: positionid (int): Position id.
    params: collapsible (int): Whether the block is collapsible.
    params: dockable (int): Whether the block is dockable.
    params: weight (Optional[int]): Used to order blocks within a region.
    params: visible (Optional[int]): Whether the block is visible.
    params: contents (BlockContent): Block contents (if required).
    """

    instanceid: int
    name: str
    region: str
    collapsible: bool
    dockable: bool
    visible: bool
    positionid: Optional[int] = None
    weight: Optional[int] = None
    contents: Optional[BlockContent] = None

    def __str__(self) -> str:
        return self.name


@dataclass
class Blocks(ResponsesFactory[Block]):
    """Blocks information for a course.
    params: blocks (List[Block]): List of blocks in the course.
    params: warnings (List[Warning]): warning
    """

    blocks: List[Block] = field(factory=list)
    warnings: List[MoodleWarning] = field(factory=list)

    @property
    def items(self) -> List[Block]:
        return self.blocks
