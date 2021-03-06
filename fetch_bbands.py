import requests, json
from flask import render_template
from app import app

def graph(symbol, period):

	technical = ["Real Upper Band", "Real Lower Band", "Real Middle Band"]
	values = []

	if period == 'short':
		last = 15
	else:
		last = 31

	for x in technical:
		fetch = "https://www.alphavantage.co/query?function=BBANDS&symbol="+symbol+"&interval=daily&time_period="+str(last-1)+"&series_type=close&apikey="
		r = requests.get(fetch+app.config['API_KEY'])
		data = r.json()
		count = 0
		for date in data["Technical Analysis: BBANDS"].keys():
			count = count + 1
			if count == last:
				break
			else:
				value = float(data["Technical Analysis: BBANDS"][date][x])
				values.append(value)
	return values
