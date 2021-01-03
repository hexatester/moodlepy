from typing import Any, List

from moodle import BaseMoodle
from moodle.utils.helper import from_dict
from . import (
    BackupCompletionStatus,
    CopyData,
    CopyDataResponse,
)
from .table_row_data import TableRowData


class BaseBackup(BaseMoodle):
    def get_async_backup_links_backup(self, filename: str,
                                      contextid: int) -> TableRowData:
        """Gets the data to use when updating the status table row in the UI for when an async backup completes.

        Args:
            filename (str): Backup filename
            contextid (int): Context id

        Returns:
            TableRowData: Table row data.
        """
        data = self.moodle.post(
            'core_backup_get_async_backup_links_backup',
            filename=filename,
            contextid=contextid,
        )
        return from_dict(TableRowData, data)

    def get_async_backup_links_restore(self, backupid: str,
                                       contextid: int) -> str:
        """Gets the data to use when updating the status table row in the UI for when an async restore completes.

        Args:
            backupid (str): Backup id
            contextid (int): Context id

        Returns:
            str: Restore url
        """
        data = self.moodle.post(
            'core_backup_get_async_backup_links_restore',
            backupid=backupid,
            contextid=contextid,
        )
        return dict(data).get('restoreurl', '')

    def get_async_backup_progress(
            self, backupids: List[str],
            contextid: int) -> List[BackupCompletionStatus]:
        """Get the progress of an Asyncronhous backup.

        Args:
            backupids (List[str]): Backup id(s) to get progress for
            contextid (int): Context id

        Returns:
            List[BackupCompletionStatus]: Backup data
        """
        data = self.moodle.post(
            'core_backup_get_async_backup_progress',
            backupids=backupids,
            contextid=contextid,
        )
        return [from_dict(BackupCompletionStatus, dat) for dat in data]

    def get_copy_progress(self,
                          copies: List[CopyData]) -> List[CopyDataResponse]:
        """Gets the progress of course copy operations.

        Args:
            copies (List[CopyData]): Copy data

        Returns:
            List[CopyDataResponse]: Copy data completion statuses
        """
        data = self.moodle.post(
            'core_backup_get_copy_progress',
            copies=copies,
        )
        return [from_dict(CopyDataResponse, dat) for dat in data]

    def submit_copy_form(self, jsonformdata: str) -> Any:
        """Handles ajax submission of course copy form.

        Args:
            jsonformdata (str): The data from the create copy form, encoded as a json array

        Returns:
            Any: JSON response.
        """
        data = self.moodle.post(
            'core_backup_submit_copy_form',
            jsonformdata=jsonformdata,
        )
        return data
