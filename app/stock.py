from app import app
from flask import render_template, request, redirect, url_for
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
		return redirect(url_for('averages'), code=307)
	else:
		return render_template('index.html')

@app.route("/averages", methods=['GET', 'POST'])
def averages():
	symbol = request.form['symbol']
	symbol = symbol.upper()
	technical = ["SMA", "WMA", "EMA"]
	values = []
	for x in technical:
	    fetch = "https://www.alphavantage.co/query?function="+x+"&symbol="+symbol+"&interval=daily&time_period=14&series_type=open&apikey="
	    APIkey = "NYZSIAK5PJ3XRW8A"
	    r = requests.get(fetch+APIkey)
	    data = r.json()
	    for time in range(1, 15):
	        kal = dt.date.today() - timedelta(time)
	        if calendar.day_name[kal.weekday()] == 'Sunday' or calendar.day_name[kal.weekday()] == "Saturday" or kal in holidays.UnitedStates():
	            continue
	        else:
	            value = float(data["Technical Analysis: "+x][kal.strftime("%Y-%m-%d")][x])
	            values.append(value)
	SMA = values[:9]
	WMA = values[9:18]
	EMA = values[18:]
	return render_template('averages.html', sma=SMA, wma=WMA, ema=EMA)

@app.route("/company2")
def company2():
	return render_template('company2.html')

@app.route("/company3")
def company3():
	return render_template('company3.html')

if __name__ == '__main__':
	app.run(debug=True)
