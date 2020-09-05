from moodle import Moodle
from moodle.core.badges import Badge


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
            assert isinstance(badge, Badge)
