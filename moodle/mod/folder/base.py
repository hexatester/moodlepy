from typing import List

from moodle import BaseMoodle
from . import Folders, View


class BaseFolder(BaseMoodle):
    def get_folders_by_courses(self, courseids: List[int]) -> Folders:
        """Returns a list of folders in a provided list of courses, if no list is provided all folders that the user can view will be returned.
        Please note that this WS is not returning the folder contents.

        Args:
            courseids (List[int]): Array of course ids

        Returns:
            Folders: List of Folder
        """
        res = self.moodle.post("mod_folder_get_folders_by_courses")
        return self._tr(Folders, **res)

    def view_folder(self, folderid: int) -> View:
        """Simulate the view.php web interface folder: trigger events, completion, etc...

        Args:
            folderid (int): folder instance id

        Returns:
            View: Response
        """
        res = self.moodle.post("mod_folder_view_folder")
        return self._tr(View, **res)
