from newsapi import NewsApiClient
from app import app

newsapi = NewsApiClient(api_key=app.config['NEWS_KEY'])

name = {
        'AAPL':'Apple',
        'MSFT':'Microsoft',
        'KO':'Coca-Cola',
        'GES':'Guess',
        'SNAP':'Snapchat',
        'DELL':'Dell',
        'SHLD':'Sears',
        'JPM':'JPMorgan',
        'BBBY':'Bed Bath and Beyond',
        'DAL':'Delta'}

def fetch(symbol):
    top_headlines = newsapi.get_top_headlines(q=name[symbol], language='en')
    return top_headlines
