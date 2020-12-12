import json
import urllib
import requests


def get_programming_language(language):
    search_param = language[0].capitalize() + language[1:]
    query = """
    {
        "ProgrammingLanguage": {
            "$regex": "%s"
        }
    }
    """ % (search_param)
    where = urllib.parse.quote_plus(query)
    url = 'https://parseapi.back4app.com/classes/ProgrammingLanguages_All_Programming_Languages?limit=10&where=%s' % where
    headers = {
        'X-Parse-Application-Id': 'EupV0l2olwm4B4q5lbz5OAW90cl8QaDtMbiGgvd5', # This is your app's application id
        'X-Parse-REST-API-Key': 'SNh8baKRcavcwh8MPmzUjKPPndgCi6KfppFM9N8K' # This is your app's REST API key
    }
    data = json.loads(requests.get(url, headers=headers).content.decode('utf-8')) # Here you have the data that you need
    return data