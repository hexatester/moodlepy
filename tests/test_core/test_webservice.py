from moodle.core.webservice import SiteInfo


class TestWebservice:
    def test_get_site_info(self, moodle, domain):
        site_info = moodle.core.webservice.get_site_info()
        assert isinstance(site_info, SiteInfo)
        assert site_info.siteid == 1
        assert site_info.siteurl == domain
        assert site_info.sitecalendartype == 'gregorian'
        assert site_info.usercalendartype == 'gregorian'
        assert site_info.usercanmanageownfiles is True
