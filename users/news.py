# codinghorror https://api.rss2json.com/v1/api.json?rss_url=https%3A%2F%2Fblog.codinghorror.com%2Frss%2F
# https://www.reddit.com/r/programming/comments/66678/ask_reddit_what_csprogramming_rss_feeds_should_i/

import urllib
import json
import users.config as config


def show_news(news_source):
    """return json response of news"""
    response = urllib.request.urlopen(config.NEWS_SITES[news_source])
    data = json.loads(response.read())
    return data
