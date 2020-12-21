from moodle.base.general import GeneralStatus


class AgreeSitePolicyResponse(GeneralStatus):
    """Agree the site policy for the current user.

    Args:
        status (int): Status: true only if we set the policyagreed to 1 for the user
        warnings (List[Warning]): list of warnings
    """
    pass
