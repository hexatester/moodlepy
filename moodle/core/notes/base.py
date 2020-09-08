from typing import List
from moodle import BaseMoodle, Warning
from moodle.utils.helper import from_dict
from . import Note, CourseNotes, ViewNotes


class BaseNotes(BaseMoodle):
    def create_notes(self, notes: List[Note]) -> List[Note.Result]:
        """Create notes

        Args:
            notes (List[Note]): Notes to create

        Returns:
            List[Note.Result]: Create note result
        """
        res = self.moodle.post('core_notes_create_notes', notes=notes)
        return [from_dict(Note.Result, data) for data in res] if res else []

    def delete_notes(self, notes: List[int]) -> List[Warning]:
        """Delete notes

        Args:
            notes (List[int]): Array of Note Ids to be deleted.

        Returns:
            List[Warning]: list of warnings
        """
        res = self.moodle.post('core_notes_delete_notes', notes=notes)
        return [from_dict(Warning, data) for data in res] if res else []

    def get_course_notes(self, courseid: int, userid: int = 0) -> CourseNotes:
        """Returns all notes in specified course (or site), for the specified user.

        Args:
            courseid (int): course id, 0 for SITE
            userid (int, optional): user id. Defaults to 0.

        Returns:
            CourseNotes: Course note object
        """
        res = self.moodle.post('core_notes_get_course_notes',
                               courseid=courseid,
                               userid=userid)
        return from_dict(CourseNotes, res)

    def view_notes(self, courseid: int, userid: int = 0) -> ViewNotes:
        """Simulates the web interface view of notes/index.php: trigger events.

        Args:
            courseid (int): course id, 0 for notes at system level
            userid (int, optional): user id, 0 means view all the user notes. Defaults to 0.

        Returns:
            ViewNotes: view notes response
        """
        res = self.moodle.post('core_notes_view_notes',
                               courseid=courseid,
                               userid=userid)
        return from_dict(ViewNotes, res)
