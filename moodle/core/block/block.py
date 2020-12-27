from dataclasses import dataclass, field
from typing import List, Optional
from moodle import MoodleWarning, ResponsesFactory


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
    filename: Optional[str]
    filepath: Optional[str]
    filesize: Optional[int]
    fileurl: Optional[str]
    timemodified: Optional[int]
    mimetype: Optional[str]
    isexternalfile: Optional[int]
    repositorytype: Optional[str]


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
    footer: Optional[str]
    files: List[BlockFile] = field(default_factory=list)

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
    positionid: Optional[int]
    collapsible: bool
    dockable: bool
    weight: Optional[int]
    visible: bool
    contents: Optional[BlockContent]

    def __str__(self) -> str:
        return self.name


@dataclass
class Blocks(ResponsesFactory[Block]):
    """Blocks information for a course.
    params: blocks (List[Block]): List of blocks in the course.
    params: warnings (List[Warning]): warning
    """
    blocks: List[Block] = field(default_factory=list)
    warnings: List[MoodleWarning] = field(default_factory=list)

    @property
    def items(self) -> List[Block]:
        return self.blocks
