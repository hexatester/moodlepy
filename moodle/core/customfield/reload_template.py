from dataclasses import dataclass
from typing import List


@dataclass
class Field:
    """Field

    Args:
        name (str): name
        shortname (str): shortname
        type (str): type
        editfieldurl (str): edit field url
        id (int): id
    """
    name: str
    shortname: str
    type: str
    editfieldurl: str
    id: int


@dataclass
class Category:
    """Category

    Args:
        id (int): id
        nameeditable (str): inplace editable name
        addfieldmenu (str): addfieldmenu
        fields (List[Field]): list of Field
    """
    id: int
    nameeditable: str
    addfieldmenu: str
    fields: List[Field]


@dataclass
class ReloadTemplate:
    """Reloaded Template

    Args:
        component (str): component
        area (str): area
        itemid (int): itemid
        usescategories (int): view has categories
        categories (List[Category]): list of Category
    """
    component: str
    area: str
    itemid: int
    usescategories: int
    categories: List[Category]
