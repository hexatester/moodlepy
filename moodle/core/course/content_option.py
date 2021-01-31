from moodle.attr import dataclass
from typing import Union


@dataclass
class ContentOption:
    """Options, used since Moodle 2.9

    Args:
        name (str): The expected keys (value format) are:
                    excludemodules (bool) Do not return modules, return only the sections structure
                    excludecontents (bool) Do not return module contents (i.e: files inside a resource)
                    includestealthmodules (bool) Return stealth modules for students in a special
                        section (with id -1)
                    sectionid (int) Return only this section
                    sectionnumber (int) Return only this section with number (order)
                    cmid (int) Return only this module information (among the whole sections structure)
                    modname (string) Return only modules with this name "label, forum, etc..."
                    modid (int) Return only the module with this id (to be used with modname
        value (Union[str, int, bool]): the value of the option, this param is personaly validated in the external function.
    """
    name: str
    value: Union[str, int, bool]

    def __str__(self):
        return self.name
