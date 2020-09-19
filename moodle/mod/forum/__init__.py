from .discussion import Discussion, Discussions
from .forum import Forum
from .post import (AuthorUrls, GroupUrls, Group, PlagiarismHtml,
                   AttachmentUrls, TagUrls, RatingInfo, Html, Tag, Attachment,
                   PostUrls, Capability, Author, Post, Message, NewPost, Posts)

from .base import BaseForum

__all__ = [
    'Discussion', 'Discussions', 'Forum', 'AuthorUrls', 'GroupUrls', 'Group',
    'PlagiarismHtml', 'AttachmentUrls', 'TagUrls', 'RatingInfo', 'Html', 'Tag',
    'Attachment', 'PostUrls', 'Capability', 'Author', 'Post', 'Message',
    'NewPost', 'Posts', 'BaseForum'
]
