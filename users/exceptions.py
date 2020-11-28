from rest_framework.exceptions import APIException

class ScoreNot100(APIException):
    status_code = 503
    default_detail = 'Total score must be 100'
    default_code = 'score_not_100'