from newsapi.newsapi_client import NewsApiClient
import twitterfetch
from textblob import TextBlob
from app import app
import datetime
from datetime import timedelta, date
import fetch_name
newsapi = NewsApiClient(api_key=app.config['NEWS_KEY'])

name = {
		'AAPL':'Apple',
		'MSFT':'Microsoft',
		'KO':'Coca-Cola',
		'GES':'Guess',
		'DELL':'Dell',
		'SHLD':'Sears',
		'JPM':'JPMorgan',
		'BBBY':'Bed Bath and Beyond',
		'DAL':'Delta'}

def fetch(symbol):
	if symbol in name.keys():
		tweetPolarity = twitterfetch.fetch(name[symbol])
		top_headlines = newsapi.get_everything(q=name[symbol], language='en', sort_by='publishedAt', from_param=str(datetime.date.today() - timedelta(1)))
	else:
		tweetPolarity = twitterfetch.fetch(fetch_name.fetch(symbol))
		top_headlines = newsapi.get_everything(q=fetch_name.fetch(symbol), language='en', sort_by='publishedAt', from_param=str(datetime.date.today() - timedelta(1)))
	number = top_headlines['totalResults']
	newsPolarity = 0
	for x in range(10):
		article = top_headlines['articles'][x]['title']
		analysis = TextBlob(article)
		newsPolarity += analysis.sentiment.polarity
	return ((newsPolarity/number)+(tweetPolarity)/2)
