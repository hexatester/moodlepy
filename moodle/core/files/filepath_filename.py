from moodle.attr import dataclass


@dataclass
class FilepathFilename:
    """Files or directories to be deleted.

    Args:
        filepath (str): Path to the file or directory to delete.
        filename (str): Name of the file to delete.
    """

    filepath: str
    filename: str
