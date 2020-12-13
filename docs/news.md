

News sites can be linked to users so as their prefered news source. If no prefered news source is set then a default one will be chosen for the user. Users with prefered news sources will be able to see their news in their profile.

The current supported news sources are:

```
news_sites = {
    "codinghorror": "https://api.rss2json.com/v1/api.json?rss_url=https%3A%2F%2Fblog.codinghorror.com%2Frss%2F",
    "lambda": "https://api.rss2json.com/v1/api.json?rss_url=http%3A%2F%2Flambda-the-ultimate.org%2Frss.xml",
    "bliki": "https://api.rss2json.com/v1/api.json?rss_url=http%3A%2F%2Fmartinfowler.com%2Fbliki%2Fbliki.atom",
    "joe": "https://api.rss2json.com/v1/api.json?rss_url=http%3A%2F%2Fwww.joelonsoftware.com%2Frss.xml",
    "feed": "https://api.rss2json.com/v1/api.json?rss_url=http%3A%2F%2Ffeeds.feedburner.com%2Ffreetechbooks",
    "orilly": "https://api.rss2json.com/v1/api.json?rss_url=http%3A%2F%2Fradar.oreilly.com%2Findex.rdf",
    "paul": "https://api.rss2json.com/v1/api.json?rss_url=http%3A%2F%2Ffeeds.feedburner.com%2FPaulGrahamUnofficialRssFeed",
    "reddit_programming": "https://www.reddit.com/r/programming/.json"
}
```