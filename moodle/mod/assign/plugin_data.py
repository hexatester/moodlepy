from moodle.attr import dataclass
from typing import Optional


@dataclass
class EditorStructure:
    """Editor structure
    Args:
        text (str): The text for this feedback.
        format (int): The format for this feedback
    """
    text: str
    format: int


@dataclass
class PluginData:
    """Plugin Data
    Args:
        assignfeedbackcomments_editor (Optional[EditorStructure]): Editor structure
        files_filemanager (Optional[int]): The id of a draft area containing files for this feedback.
    """
    assignfeedbackcomments_editor: Optional[EditorStructure]
    files_filemanager: Optional[int]
