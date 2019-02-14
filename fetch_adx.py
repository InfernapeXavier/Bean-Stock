import requests, json
from flask import render_template

APIKey = "NYZSIAK5PJ3XRW8A"

def graph(symbol, period):

	values = []
	count = 0

	if period == 'short':
		last = 15
	else:
		last = 31

	fetch = "https://www.alphavantage.co/query?function=ADX&symbol="+symbol+"&interval=daily&time_period="+str(last-1)+"&series_type=open&apikey="
	r = requests.get(fetch+APIKey)
	data = r.json()

	for date in data["Technical Analysis: ADX"].keys():
		count = count + 1
		if count == last:
			break
		else:
			value = float(data["Technical Analysis: ADX"][date]["ADX"])
			values.append(value)
	return values
