from dacite import from_dict
from moodle import BaseMoodle, BlogEntries


class BaseBlog(BaseMoodle):
    def get_entries(self) -> BlogEntries:
        data = self.moodle.get('core_blog_get_entries')
        return from_dict(BlogEntries, data)
