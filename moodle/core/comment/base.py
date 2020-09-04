from moodle import BaseMoodle


class BaseComment(BaseMoodle):
    def add_comments(self):
        data = self.moodle.get('core_comment_add_comments')
        return data

    def delete_comments(self):
        data = self.moodle.get('core_comment_delete_comments')
        return data

    def get_comments(self):
        data = self.moodle.get('core_comment_get_comments')
        return data
