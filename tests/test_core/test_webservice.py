from moodle import Moodle


class TestWebservice:
    domain = 'https://school.moodledemo.net'
    username = 'manager'
    password = 'moodle'

    def test_get_site_info(self):
        m = Moodle.login(self.domain, self.username, self.password)
        info = m.core.webservice.get_site_info()
        assert info.siteid == 1
        assert info.siteurl == self.domain
        assert info.username == self.username
        assert info.sitecalendartype == 'gregorian'
        assert info.usercalendartype == 'gregorian'
        assert info.usercanmanageownfiles is True
