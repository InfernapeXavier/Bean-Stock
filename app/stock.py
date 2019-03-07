from app import app
from flask import render_template, request, redirect, url_for, session
import requests, json
import datetime
from datetime import timedelta, date
import calendar, holidays
import fetch_averages, fetch_bbands, fetch_adx
import predict
import pandas as pd

@app.route("/", methods=['GET', 'POST'])
@app.route("/index/", methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		session['symbol'] = request.form['symbol'].upper()
		session['period'] = request.form['prediction']
		symbol = session.get('symbol', None)
		period = session.get('period', None)
		return redirect(url_for('averages', company=symbol, time=period))
	else:
		return render_template('index.html')

@app.route("/averages/<company>/<time>/", methods=['GET', 'POST'])
def averages(company, time):
	if request.method == 'POST':
		symbol = request.form['symbol'].upper()
		period = request.form['prediction']
		return redirect(url_for('bband', company=symbol, time=period))
	if time == 'short':
		last = 15
	else:
		last = 31
	labels = list(range(1, last))
	# labels = [(datetime.date.today() - timedelta(x)).strftime("%d/%m/%y") for x in range(0, last-1)]
	values = fetch_averages.graph(company, time)
	SMA = values[:(last-1)]
	SMA.reverse()
	WMA = values[(last-1):((last-1)*2)]
	WMA.reverse()
	EMA = values[((last-1)*2):]
	EMA.reverse()
	prediction = predict.predict(company, time)
	return render_template('averages.html', company=company, time=time, sma=SMA, wma=WMA, ema=EMA, labels=labels, prediction=prediction)

@app.route("/bband/<company>/<time>/", methods=['GET', 'POST'])
def bband(company, time):
	if request.method == 'POST':
		symbol = request.form['symbol'].upper()
		period = request.form['prediction']
		return redirect(url_for('bband', company=symbol, time=period))
	else:
		if time == 'short':
			last = 15
		else:
			last = 31
		labels = list(range(1, last))
		# labels = [(datetime.date.today() - timedelta(x)).strftime("%d/%m/%y") for x in range(0, last)]
		values = fetch_bbands.graph(company, time)
		UBB = values[:(last-1)]
		UBB.reverse()
		print (UBB)
		LBB = values[(last-1):((last-1)*2)]
		LBB.reverse()
		print (LBB)
		MBB = values[((last-1)*2):]
		MBB.reverse()
		print (MBB)
		prediction = predict.predict(company, time)
		return render_template('bband.html', company=company, time=time, ubb=UBB, mbb=MBB, lbb=LBB, labels=labels, prediction=prediction)

@app.route("/adx/<company>/<time>/", methods=['GET', 'POST'])
def adx(company, time):
	if request.method == 'POST':
		symbol = request.form['symbol'].upper()
		period = request.form['prediction']
		return redirect(url_for('adx', company=symbol, time=period))
	else:
		if time == 'short':
			last = 15
		else:
			last = 31
		labels = list(range(1, last))
		# labels = [(datetime.date.today() - timedelta(x)).strftime("%d/%m/%y") for x in range(0, last)]
		ADX = fetch_adx.graph(company, time)
		ADX.reverse()
		prediction = predict.predict(company, time)
		return render_template('adx.html', company=company, time=time, adx=ADX, labels=labels, prediction=prediction)

if __name__ == '__main__':
	app.run(debug=True)
