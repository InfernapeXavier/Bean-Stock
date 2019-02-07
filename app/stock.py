from app import app
from flask import render_template, request, redirect, url_for, session
import requests
import json
import datetime as dt
from datetime import timedelta, date
import calendar
import holidays

@app.route("/", methods=['GET', 'POST'])
@app.route("/index", methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		session['symbol'] = request.form['symbol'].upper()
		return redirect(url_for('averages'), code=307)
	else:
		return render_template('index.html')

@app.route("/averages", methods=['GET', 'POST'])
def averages():
	symbol = session.get('symbol', None)
	technical = ["SMA", "WMA", "EMA"]
	values = []
	for x in technical:
		fetch = "https://www.alphavantage.co/query?function="+x+"&symbol="+symbol+"&interval=daily&time_period=14&series_type=open&apikey="
		APIkey = "NYZSIAK5PJ3XRW8A"
		r = requests.get(fetch+APIkey)
		data = r.json()
		count = 0
		for date in data["Technical Analysis: "+x].keys():
			count = count + 1
			if count == 15:
				break
			else:
				value = float(data["Technical Analysis: "+x][date][x])
				values.append(value)
	SMA = values[:14]
	WMA = values[14:28]
	EMA = values[28:]
	return render_template('averages.html', sma=SMA, wma=WMA, ema=EMA)

@app.route("/bband", methods=['GET', 'POST'])
def bband():
	if request.method == 'POST':
		session['symbol'] = request.form['symbol'].upper()
		return redirect(url_for('bband'), code=307)
	else:
		symbol = session.get('symbol', None)
		technical = ["Real Upper Band", "Real Lower Band", "Real Middle Band"]
		values = []
		for x in technical:
			fetch = "https://www.alphavantage.co/query?function=BBANDS&symbol="+symbol+"&interval=daily&time_period=14&series_type=open&apikey="
			APIkey = "NYZSIAK5PJ3XRW8ASSS"
			r = requests.get(fetch+APIkey)
			data = r.json()
			count = 0
			for date in data["Technical Analysis: BBANDS"].keys():
				count = count + 1
				if count == 15:
					break
				else:
					value = float(data["Technical Analysis: BBANDS"][date][x])
					values.append(value)
		UBB = values[:14]
		LBB = values[14:28]
		MBB = values[28:]
		return render_template('bband.html', ubb=UBB, mbb=MBB, lbb=LBB)

@app.route("/adx", methods=['GET', 'POST'])
def adx():
	if request.method == 'POST':
		session['symbol'] = request.form['symbol'].upper()
		return redirect(url_for('adx'), code=307)
	else:
		symbol = session.get('symbol', None)
		values = []
		fetch = "https://www.alphavantage.co/query?function=ADX&symbol="+symbol+"&interval=daily&time_period=14&series_type=open&apikey="
		APIkey = "NYZSIAK5PJ3XRW8ASSS"
		r = requests.get(fetch+APIkey)
		data = r.json()
		count = 0
		for date in data["Technical Analysis: ADX"].keys():
			count = count + 1
			if count == 15:
				break
			else:
				value = float(data["Technical Analysis: ADX"][date]["ADX"])
				values.append(value)
		ADX = values
		return render_template('adx.html', adx=ADX)

if __name__ == '__main__':
	app.run(debug=True)
