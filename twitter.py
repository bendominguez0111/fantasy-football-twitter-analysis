import requests, pprint
from requests_oauthlib import OAuth1
from urllib import parse
from config import Config

config = Config()

def generate_oauth1():
    oauth = OAuth1(config.TWITTER_API_KEY, config.TWITTER_SECRET_KEY, config.TWITTER_ACCESS_TOKEN, config.TWITTER_ACCESS_SECRET)
    return oauth

def generate_tweets(search, analysts=config.ANALYSTS):

    oauth = generate_oauth1()

    ## build URL
    url = config.SEARCH_BASE_URL + '?q='
    from_accounts = 'from:'
    for i, account in enumerate(analysts.values()):
        if i == 0:
            from_accounts = from_accounts + account
        else:
            from_accounts = from_accounts + ' OR ' + account

    search_values = ''
    for i, val in enumerate(search):
        if i == 0:
            search_values = search_values + val
        else:
            search_values = search_values + ' OR ' + account

    first_query = parse.quote(from_accounts + search_values)

    url = url + first_query

    SEARCH_PARAMS = {
        'count': '100',
        'lang': 'en',
        'include_entities': False
    }

    res = requests.get(
        url,
        params=SEARCH_PARAMS,
        auth=oauth
    )

    tweets = res.json().get('statuses')

    parsed_tweets = []

    for tweet in tweets:
        truncated = tweet.get('truncated')
        text = tweet.get('text')

        if not truncated and 'RT' not in text:
            parsed_tweets.append(text)

    return parsed_tweets

#test code down here.
if __name__ == '__main__':
    print(generate_tweets("Henry"))
