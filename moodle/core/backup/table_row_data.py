from dataclasses import dataclass


@dataclass
class TableRowData:
    """Table row data.

    Args:
        filesize (str): Backup file size
        fileurl (str): Backup file URL
        restoreurl (str): Backup restore URL
    """
    filesize: str
    fileurl: str
    restoreurl: str
