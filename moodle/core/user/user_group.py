from dataclasses import dataclass


@dataclass
class UserGroup:
    """User Group

    Args:
        id (int): group id
        name (str): group name
        description (str): group description
        descriptionformat (int): description format (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
    """
    id: int
    name: str
    description: str
    descriptionformat: int
