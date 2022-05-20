from typing import List, Optional
from moodle import BaseMoodle

from . import Book, Books, View


class BaseBook(BaseMoodle):
    def get_books_by_courses(self, courseids: List[int]) -> Books:
        """Returns a list of book instances in a provided set of courses, if no courses are provided then all the book instances the user has access to will be returned.

        Args:
            courseids (List[int]): Array of course ids

        Returns:
            Books: List of Book
        """
        res = self.moodle.post(
            "mod_book_get_books_by_courses",
            courseids=courseids,
        )
        return self._tr(Books, **res)

    def view_book(self, bookid: int, chapterid: int = 0) -> View:
        """Simulate the view.php web interface book: trigger events, completion, etc...

        Args:
            bookid (int): book instance id
            chapterid (int, optional): chapter id. Defaults to 0.

        Returns:
            View: Response of view book
        """
        res = self.moodle.post(
            "mod_book_view_book",
            bookid=bookid,
            chapterid=chapterid,
        )
        return self._tr(View, **res)
