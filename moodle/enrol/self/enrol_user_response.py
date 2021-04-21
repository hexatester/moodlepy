from moodle.base.general import GeneralStatus


class EnrolUserResponse(GeneralStatus):
    """Enrol User Response

    Args:
        status (int): status: true if the user is enrolled, false otherwise
        warnings (List[MoodleWarning]): list of warnings
    """

    pass
