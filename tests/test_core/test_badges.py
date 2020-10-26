from moodle import Moodle
from moodle.core.badges.badge import BagdeAlignment, BagdeEndorsement, RelatedBadge


class TestBadges:
    def test_get_user_badges(self, moodle: Moodle):
        badges = moodle.core.bagdes.get_user_badges()
        assert len(badges) == 0
        assert len(badges.badges) == 0
        assert len(badges.warnings) == 0

        badges = moodle.core.bagdes.get_user_badges(userid=56)
        assert len(badges) == 5
        assert len(badges.badges) == 5
        assert len(badges.warnings) == 0
        for badge in badges:
            assert not badge.id or isinstance(badge.id, int)
            assert isinstance(badge.name, str)
            assert isinstance(badge.description, str)
            assert not badge.timecreated or isinstance(badge.timecreated, int)
            assert not badge.timemodified or isinstance(
                badge.timemodified, int)
            assert not badge.usercreated or isinstance(badge.usercreated, int)
            assert not badge.usermodified or isinstance(
                badge.usermodified, int)
            assert isinstance(badge.issuername, str)
            assert isinstance(badge.issuerurl, str)
            assert isinstance(badge.issuercontact, str)
            assert not badge.expiredate or isinstance(badge.expiredate, int)
            assert not badge.expireperiod or isinstance(
                badge.expireperiod, int)
            assert not badge.type or isinstance(badge.type, int)
            assert not badge.courseid or isinstance(badge.courseid, int)
            assert not badge.message or isinstance(badge.message, str)
            assert not badge.messagesubject or isinstance(
                badge.messagesubject, str)
            assert not badge.attachment or isinstance(badge.attachment, int)
            assert not badge.notification or isinstance(
                badge.notification, int)
            assert not badge.nextcron or isinstance(badge.nextcron, int)
            assert not badge.status or isinstance(badge.status, int)
            assert not badge.issuedid or isinstance(badge.issuedid, int)
            assert isinstance(badge.uniquehash, str)
            assert isinstance(badge.dateissued, int)
            assert not badge.dateexpire or isinstance(badge.dateexpire, int)
            assert not badge.visible or isinstance(badge.visible, int)
            assert not badge.email or isinstance(badge.email, str)
            assert not badge.version or isinstance(badge.version, str)
            assert not badge.language or isinstance(badge.language, str)
            assert not badge.imageauthorname or isinstance(
                badge.imageauthorname, str)
            assert not badge.imageauthoremail or isinstance(
                badge.imageauthoremail, str)
            assert not badge.imageauthorurl or isinstance(
                badge.imageauthorurl, str)
            assert not badge.imagecaption or isinstance(
                badge.imagecaption, str)
            assert isinstance(badge.badgeurl, str)
            assert not badge.endorsement or isinstance(badge.endorsement,
                                                       BagdeEndorsement)
            for alignment in badge.alignment:
                assert isinstance(alignment, BagdeAlignment)
                assert not alignment.id or isinstance(alignment.id, int)
                assert not alignment.badgeid or isinstance(
                    alignment.badgeid, int)
                assert not alignment.targetName or isinstance(
                    alignment.targetName, str)
                assert not alignment.targetUrl or isinstance(
                    alignment.targetUrl, str)
                assert not alignment.targetDescription or isinstance(
                    alignment.targetDescription, str)
                assert not alignment.targetFramework or isinstance(
                    alignment.targetFramework, str)
                assert not alignment.targetCode or isinstance(
                    alignment.targetCode, str)
            for related_badge in badge.relatedbadges:
                assert isinstance(related_badge, RelatedBadge)
                assert isinstance(related_badge.id, int)
                assert isinstance(related_badge.name, str)
                assert not related_badge.version or isinstance(
                    related_badge.version, str)
                assert not related_badge.language or isinstance(
                    related_badge.language, str)
                assert not related_badge.type or isinstance(
                    related_badge.type, int)
