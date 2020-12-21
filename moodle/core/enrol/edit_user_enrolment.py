from moodle.base.general import GeneralResultError


class EditUserEnrolmentResponse(GeneralResultError):
    """[summary]

    Args:
        result (int): True if the user's enrolment was successfully updated
        errors (List[GeneralKeyMessage]): List of validation errors
    """
    pass
