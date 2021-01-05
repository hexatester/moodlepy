from moodle import Moodle
from moodle.core.block import BlockContent, Block, Blocks


class TestBlock:
    def test_get_courses(self):
        # TODO Test for core_block_get_course_blocks
        pass

    def test_get_dashboard_blocks(self, moodle: Moodle):
        blocks = moodle.core.block.get_dashboard_blocks()
        assert isinstance(blocks, Blocks)
        for block in blocks:
            assert isinstance(block, Block)
            assert isinstance(block.instanceid, int)
            assert isinstance(block.name, str)
            assert isinstance(block.region, str)
            assert type(block.collapsible) == bool
            assert type(block.dockable) == bool
            assert type(block.visible) == bool
            assert not block.contents or type(block.contents) == BlockContent
            assert not block.positionid or isinstance(block.positionid, int)
            assert not block.weight or isinstance(block.weight, int)
