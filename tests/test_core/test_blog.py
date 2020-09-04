from moodle import Moodle


class TestBlogEntry:
    id = 5
    module = 'blog'
    userid = 100
    courseid = 0
    groupid = 0
    moduleid = 0
    coursemoduleid = 0
    subject = 'My homework blog'
    summary = '<p>I just found this blog and I thought I would start it to keep a record of my homework. I will try to remember to do it? (I wonder if this will be seen by everybody?)</p>'  # NOQA
    summaryformat = 1
    content = None
    uniquehash = ''
    rating = 0
    format = 1
    attachment = ''
    publishstate = 'site'
    lastmodified = 1411642656
    created = 1411642655
    usermodified = None
    summaryfiles = []
    attachmentfiles = []
    tags = []

    def test_get_entries(self, moodle: Moodle):
        entries = moodle.core.blog.get_entries()
        entry = entries.first()
        assert entry.id == self.id
        assert entry.module == self.module
        assert entry.userid == self.userid
        assert entry.courseid == self.courseid
        assert entry.groupid == self.groupid
        assert entry.moduleid == self.moduleid
        assert entry.coursemoduleid == self.coursemoduleid
        assert entry.subject == self.subject
        assert entry.summary == self.summary
        assert entry.summaryformat == self.summaryformat
        assert entry.content == self.content
        assert entry.uniquehash == self.uniquehash
        assert entry.rating == self.rating
        assert entry.format == self.format
        assert entry.attachment == self.attachment
        assert entry.publishstate == self.publishstate
        assert entry.lastmodified == self.lastmodified
        assert entry.created == self.created
        assert entry.usermodified == self.usermodified
        assert entry.summaryfiles == self.summaryfiles
        assert entry.attachmentfiles == self.attachmentfiles
        assert entry.tags == self.tags

    def test_view_entries(self, moodle: Moodle):
        res = moodle.core.blog.view_entries()
        assert res is True
