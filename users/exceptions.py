from rest_framework.exceptions import APIException
import users.config as config

class ScoreNot100(APIException):
    status_code = 400
    default_detail = 'Total score must be 100'
    default_code = 'score_not_100'

class ProfileNotCreated(APIException):
    status_code = 400
    default_detail = 'Must create a profile before executing this action'
    default_code = 'profile_non_existant'

class CannotCreateSameLanguage(APIException):
    status_code = 400
    default_detail = 'Cannot add the same language more than once'
    default_code = 'cannot_add_same_language'

class NewsSourceNotAvailable(APIException):
    status_code = 400
    default_detail = f'News source not available, please use one of the available news sources {config.NEWS_SITES}'
    default_code = 'cannot_add_same_language'

class LanguageNotFound(APIException):
    def __init__(self, results):
        self.results = results
        self.detail = f'The language you entered cannot be found, however we found these instead {self.results}'

    status_code = 400
    default_code = 'cannot_add_same_language'