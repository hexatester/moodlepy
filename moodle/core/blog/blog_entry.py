from dataclasses import dataclass, field
from typing import Any, Iterator, List, Optional
from moodle import Warning


@dataclass
class BlogEntry:
    id: int
    module: str
    userid: int
    courseid: int
    groupid: int
    moduleid: int
    coursemoduleid: int
    subject: str
    summary: str
    summaryformat: int
    content: Optional[Any]
    uniquehash: str
    rating: int
    format: int
    attachment: str
    publishstate: str
    lastmodified: int
    created: int
    usermodified: Optional[Any]
    summaryfiles: list = field(default_factory=list)
    attachmentfiles: list = field(default_factory=list)
    tags: list = field(default_factory=list)


@dataclass
class BlogEntries:
    entries: List[BlogEntry]
    totalentries: int
    warnings: List[Warning] = field(default_factory=list)

    def __call__(self) -> List[BlogEntry]:
        return self.entries

    def __iter__(self) -> Iterator[BlogEntry]:
        return iter(self.entries)

    def __len__(self) -> int:
        return len(self.entries)

    def first(self) -> BlogEntry:
        return self.entries[0]
