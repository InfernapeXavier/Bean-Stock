import requests, json
from flask import render_template
from app import app

def graph(symbol, period):

	values = []
	count = 0

	if period == 'short':
		last = 15
	else:
		last = 31

	fetch = "https://www.alphavantage.co/query?function=ADX&symbol="+symbol+"&interval=daily&time_period="+str(last-1)+"&series_type=open&apikey="
	r = requests.get(fetch+app.config['API_KEY'])
	data = r.json()

	for date in data["Technical Analysis: ADX"].keys():
		count = count + 1
		if count == last:
			break
		else:
			value = float(data["Technical Analysis: ADX"][date]["ADX"])
			values.append(value)
	return values
