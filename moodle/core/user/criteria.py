from moodle.base.general import GeneralKeyValue


class Criteria(GeneralKeyValue):
    """the key/value pairs to be considered in user search. Values can not be empty.
        Specify different keys only once (fullname => 'user1', auth => 'manual', ...) -
        key occurences are forbidden.
        The search is executed with AND operator on the criterias. Invalid criterias (keys) are ignored,
        the search is still executed on the valid criterias.
        You can search without criteria, but the function is not designed for it.
        It could very slow or timeout. The function is designed to search some specific users.

    Args:
        key (str): the user column to search, expected keys (value format) are:
                            "id" (int) matching user id,
                            "lastname" (string) user last name (Note: you can use % for searching but it may be considerably slower!),
                            "firstname" (string) user first name (Note: you can use % for searching but it may be considerably slower!),
                            "idnumber" (string) matching user idnumber,
                            "username" (string) matching user username,
                            "email" (string) user email (Note: you can use % for searching but it may be considerably slower!),
                            "auth" (string) matching user auth plugin
        value (int, str): the value to search
    """
    pass
