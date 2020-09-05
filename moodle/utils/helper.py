def make_params(wstoken: str,
                wsfunction: str,
                moodlewsrestformat: str = 'json') -> dict:
    return {
        'wstoken': wstoken,
        'wsfunction': wsfunction,
        'moodlewsrestformat': moodlewsrestformat
    }
