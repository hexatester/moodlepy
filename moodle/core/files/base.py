from typing import List

from moodle import BaseMoodle
from .filepath_filename import FilepathFilename
from .parent_paths import ParentPaths


class BaseFiles(BaseMoodle):
    def delete_draft_files(self, draftitemid: int,
                           files: List[FilepathFilename]) -> ParentPaths:
        """Delete the indicated files (or directories) from a user draft file area.

        Args:
            draftitemid (int): Item id of the draft file area
            files (List[FilepathFilename]): Files or directories to be deleted.

        Returns:
            ParentPaths: Path(s) to parent directory of the deleted file(s)
        """
        data = self.moodle.post('core_files_delete_draft_files')
        return ParentPaths(**data)  # type: ignore

    def get_files(self,
                  contextid: int,
                  component: str,
                  filearea: str,
                  itemid: int,
                  filepath: str,
                  filename: str,
                  modified: int = None,
                  contextlevel: str = None,
                  instanceid: int = None):
        data = self.moodle.post(
            'core_files_get_files',
            contextid=contextid,
            component=component,
            filearea=filearea,
            itemid=itemid,
            filepath=filepath,
            filename=filename,
            modified=modified,
            contextlevel=contextlevel,
            instanceid=instanceid,
        )
        return data

    def upload(self,
               component: str,
               filearea: str,
               itemid: int,
               filepath: str,
               filename: str,
               filecontent: str,
               contextid: int = None,
               contextlevel: str = None,
               instanceid: int = None):
        data = self.moodle.post(
            'core_files_upload',
            component=component,
            filearea=filearea,
            itemid=itemid,
            filepath=filepath,
            filename=filename,
            filecontent=filecontent,
            contextid=contextid,
            contextlevel=contextlevel,
            instanceid=instanceid,
        )
        return data
