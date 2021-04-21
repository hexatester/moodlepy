from moodle.attr import dataclass


@dataclass
class UserCustomField:
    """UserCustomField
    Args:
        type (str): The type of the custom field
        name (str): The name of the custom field
        value (str): Custom field value, can be an encoded json if required
    """

    type: str
    name: str
    value: str
