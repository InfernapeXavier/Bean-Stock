from flask import Flask
from flask import render_template
# from test import listone
# from toFetch import SMA, WMA, EMA
import json
import requests
import datetime as dt
from datetime import timedelta, date
import calendar
import holidays

app=Flask(__name__)

SMA = []
WMA = []
EMA = []
# newstr = ''
# for element in listone:
# 	newstr = newstr + str(element)

# @app.route("/index")
@app.route("/")
def index():
	# return render_template('pg1.html', data=newstr)
	# return ''.join(str(listone())).strip(' ')
	return render_template('pg1.html')

@app.route("/pg1.html")
def pg1():
	return render_template('pg1.html')	

@app.route("/company1.html")
def company1():
	technical = ["SMA", "WMA", "EMA"]
	values = []
	for x in technical:
	    fetch = "https://www.alphavantage.co/query?function="+x+"&symbol=MSFT&interval=daily&time_period=14&series_type=open&apikey="
	    APIkey = "NYZSIAK5PJ3XRW8A"
	    r = requests.get(fetch+APIkey)
	    data = r.json()
	    print()
	    print(x)
	    for time in range(1, 15):
	        kal = dt.date.today() - timedelta(time)
	        if calendar.day_name[kal.weekday()] == 'Sunday' or calendar.day_name[kal.weekday()] == "Saturday" or kal in holidays.UnitedStates():
	            continue
	        else:
	            print(kal.strftime("%Y-%m-%d"), end=' ')
	            value = float(data["Technical Analysis: "+x][kal.strftime("%Y-%m-%d")][x])
	            values.append(value)
	            print(value)
	print()
	SMA = values[:9]
	WMA = values[9:18]
	EMA = values[18:]
	return render_template('company1.html', sma=SMA, wma=WMA, ema=EMA)
	# return render_template('company1.html')	

@app.route("/company2.html")
def company2():
	# return render_template('company2.html', datedata=datelist, valuedata=valuelist)	
	return render_template('company2.html')

@app.route("/company3.html")
def company3():
	return render_template('company3.html')	

if __name__ == '__main__':
	app.run(debug=True)

