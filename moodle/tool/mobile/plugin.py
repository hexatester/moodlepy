from moodle.attr import dataclass


@dataclass
class MobilePlugin:
    component: str
    version: str
    addon: str
    dependencies: list
    fileurl: str
    filehash: str
    filesize: int
    handlers: str
    lang: str
