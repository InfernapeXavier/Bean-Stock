import tweepy
from textblob import TextBlob

consumerKey = "dyvovX6kCCZ4CUo33hWYHABWT"
consumerSecret = "s7Csizvn47r5H0a0SmxV5kVniV7f2LN87Hy0f3PiRZIbFUJ89J"
accessToken = "4047015314-jX4Gsa4rDgrUTxKvuYFQOnxpE2osHowDEcXx7me"
accessSecret = "RsKqOskhksb7wJ2Qed50umhHAmcp66SK9t2fp75m4MOpJ"

def percentage(part, whole):
	return 100*float(part)/float(whole)

auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessSecret)
api = tweepy.API(auth)

searchTerm = input("Enter the term: ")

tweets = tweepy.Cursor(api.search, q=searchTerm).items(5)

polarity = 0

for tweet in tweets:
	analysis = TextBlob(tweet.text)
	print(analysis)
	print(analysis.sentiment)
	print()
