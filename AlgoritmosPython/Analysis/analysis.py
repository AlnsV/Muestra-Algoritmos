import tweepy
from textblob import TextBlob

consumer_key = 'z4OMjR0lY1PGYojysSZK4bLtf'
consumer_secret = 'aBBWdQK1aT4mKLIz2zbD42fLJJhQUaKqfQkUSAkEEwxcKPDWlk'

access_token = '74024384-WGOxmxPOaAApRFLTvhETyqcoXErZ7Gn2021rjtnwG'
access_token_secret = '3N5JEE32n9GcQJhqps8VbzONNVHvWYHWYcwZOqnrPnyaU'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

buscar = input("Inserte palabra clave: ")

public_tweets = api.search(buscar)

for tweet in public_tweets:
    print(tweet.text, "\n")
    analysis = TextBlob(tweet.text)
    if (analysis.sentiment.polarity)<=0:
        print("Positive \n")
    else:
        print("Negative \n")

    print(analysis.sentiment)
