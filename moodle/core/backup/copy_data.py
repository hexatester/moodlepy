from dataclasses import dataclass


@dataclass
class CopyData:
    """Copy data

    Args:
        backupid (str): Backup id
        restoreid (str): Restore id
        operation (str): Operation type
    """
    backupid: str
    restoreid: str
    operation: str


@dataclass
class CopyDataResponse:
    """Copy completion status

    Args:
        status (int): Copy Status
        progress (float): Copy progress
        backupid (str): Copy id
        operation (str): Operation type
    """
    status: int
    progress: float
    backupid: str
    operation: str
