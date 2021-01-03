from dataclasses import dataclass


@dataclass
class BackupCompletionStatus:
    """Backup completion status

    Args:
        status (int): Backup Status
        progress (float): Backup progress
        backupid (str): Backup id
        operation (str): operation type
    """
    status: int
    progress: float
    backupid: str
    operation: str
