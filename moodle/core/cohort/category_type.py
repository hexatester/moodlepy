from moodle.base.general import GeneralTypeValue


class CategoryType(GeneralTypeValue):
    """Cohort category / type

    Args:
        type (str): the name of the field: id (numeric value
                        of course category id) or idnumber (alphanumeric value of idnumber course category)
                        or system (value ignored)
        value (str): the value of the categorytype
    """
    pass
