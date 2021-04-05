from moodle import Moodle
from moodle.core.blog import BlogEntry, BlogEntries, ViewEntry


class TestBlogEntry:
    def test_get_entries(self, moodle: Moodle):
        entries = moodle.core.blog.get_entries()
        assert isinstance(
            entries,
            BlogEntries,
        )
        for entry in entries:
            assert isinstance(entry, BlogEntry)

    def test_view_entries(self, moodle: Moodle):
        res = moodle.core.blog.view_entries()
        assert isinstance(res, ViewEntry)
        assert res.status is True
