from rest_framework.exceptions import APIException


class PerformerExistValidation(APIException):
    status_code = 400
    default_detail = "Jam already has a perfomer "
    default_detail += "or Band role not in user role."
    default_code = "performer_already_exist"


class JamStartedAlreadyValidation(APIException):
    status_code = 400
    default_detail = "Jam already started or band role is not filled."
    default_code = "jam_already_started"


class JamJoinedAlreadyValidation(APIException):
    status_code = 400
    default_detail = "You already joined this jam."
    default_code = "jam_joined_already"


class JamIsPrivateValidation(APIException):
    status_code = 400
    default_detail = "This jam is a private jam."
    default_code = "jam_is_private"
