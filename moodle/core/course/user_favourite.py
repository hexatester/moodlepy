from moodle.attr import dataclass


@dataclass
class UserFavourite:
    """User Favourite

    Attributes:
        id (int): The id of the content item
        name (str): Name of the content item
        title (str): The string title of the content item, human readable
        link (str): The link to the content item creation page
        icon (str): Html containing the icon for the content item
        help (str): Html description / help for the content item
        archetype (str): The archetype of the module exposing the content item
        componentname (str): The name of the component exposing the content item
        favourite (int): Has the user favourited the content item
        legacyitem (int): If this item was pulled from the old callback and has no item id.
        recommended (int): Has this item been recommended
    """

    id: int
    name: str
    title: str
    link: str
    icon: str
    help: str
    archetype: str
    componentname: str
    favourite: int
    legacyitem: int
    recommended: int
