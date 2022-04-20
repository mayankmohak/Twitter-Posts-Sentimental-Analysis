import tweepy 
from tweepy import OAuthHandler 

CONSUMER_KEY = 'rSWOAP1MYnBM7eOOf6cB1XJXg'
CONSUMER_SECRET = 'tIMNNRLPe2xbSof6vjHWRk898brkIPPdGZwJ16y22aqxf5wWcP'
ACCESS_KEY = '1106601677220569088-Sn1frhHRheQ0uket7PJx6cIhHKrknu'
ACCESS_SECRET = 'q4EfXRzA7tmKSGW6Yl9y7xsZabvKWX2eHmCI8b16ModqS'

auth = tweepy.auth.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)

# print(dir(api))
query = "corona"
count = 5
fetched_tweets = api.search_tweets(q = query, count = count)
print(fetched_tweets)