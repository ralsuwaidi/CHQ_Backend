from rest_framework.exceptions import APIException

class ScoreNot100(APIException):
    status_code = 503
    default_detail = 'Total score must be 100'
    default_code = 'score_not_100'

class ProfileNotCreated(APIException):
    status_code = 504
    default_detail = 'Must create a profile before executing this action'
    default_code = 'profile_non_existant'

class CannotCreateSameLanguage(APIException):
    status_code = 505
    default_detail = 'Cannot add the same language more than once'
    default_code = 'cannot_add_same_language'