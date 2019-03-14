import tweepy
from textblob import TextBlob
from app import app

consumerKey = app.config['CONSUMER_KEY']
consumerSecret = app.config['CONSUMER_SECRET']
accessToken = app.config['ACCESS_TOKEN']
accessSecret = app.config['ACCESS_SECRET']

auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessSecret)
api = tweepy.API(auth)

def fetch(symbol):
	searchTerm = symbol
	tweets = tweepy.Cursor(api.search, q=searchTerm).items(100)
	polarity = 0
	for tweet in tweets:
		analysis = TextBlob(tweet.text)
		polarity += analysis.sentiment.polarity
	return (polarity/100)
