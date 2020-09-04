from dacite import from_dict
from moodle import BaseMoodle
from . import BlogEntries


class BaseBlog(BaseMoodle):
    def get_entries(self) -> BlogEntries:
        data = self.moodle.get('core_blog_get_entries')
        return from_dict(BlogEntries, data)

    def view_entries(self) -> bool:
        data = self.moodle.get('core_blog_view_entries')
        if data:
            return data.get('status')
        return False
