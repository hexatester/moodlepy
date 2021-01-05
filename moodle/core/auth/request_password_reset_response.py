from moodle.attr import dataclass
from typing import List
from moodle import MoodleWarning


@dataclass
class RequestPasswordResetResponse:
    """RequestPasswordResetResponse

    Args:
        status (str): The returned status of the process:
                        dataerror: Error in the sent data (username or email). More information in warnings field.
                        emailpasswordconfirmmaybesent: Email sent or not (depends on user found in database).
                        emailpasswordconfirmnotsent: Failure, user not found.
                        emailpasswordconfirmnoemail: Failure, email not found.
                        emailalreadysent: Email already sent.
                        emailpasswordconfirmsent: User pending confirmation.
                        emailresetconfirmsent: Email sent.
        notice (str): Important information for the user about the process.
        warnings (List[Warning]): list of warnings
    """
    status: str
    notice: str
    warnings: List[MoodleWarning]
