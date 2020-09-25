from typing import List
from moodle import BaseMoodle
from moodle.utils.helper import from_dict
from . import Resources, View


class BaseResource(BaseMoodle):
    def get_resources_by_courses(self, courseids: List[int]) -> Resources:
        """Returns a list of files in a provided list of courses, if no list is provided all files that the user can view will be returned.

        Args:
            courseids (List[int]): Array of course ids

        Returns:
            Resources: List of Resource
        """
        res = self.moodle.post('mod_resource_get_resources_by_courses',
                               courseids=courseids)
        return from_dict(Resources, res)

    def view_resource(self, resourceid: int) -> View:
        """Simulate the view.php web interface resource: trigger events, completion, etc...

        Args:
            resourceid (int): resource instance id

        Returns:
            View: View Resource response
        """
        res = self.moodle.post('mod_resource_view_resource',
                               resourceid=resourceid)
        return from_dict(View, res)
