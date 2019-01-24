import flask
import json
import requests
import datetime as dt
from datetime import timedelta, date
import calendar
app = flask.Flask(__name__)

technical = ["SMA", "WMA", "EMA"]
for x in technical:
    fetch = "https://www.alphavantage.co/query?function="+x+"&symbol=MSFT&interval=daily&time_period=10&series_type=open&apikey="
    APIkey = "NYZSIAK5PJ3XRW8A"
    r = requests.get(fetch+APIkey)
    data = r.json()
    print()
    print(x)
    for time in range(1, 15):
        kal = dt.date.today() - timedelta(time)
        if calendar.day_name[kal.weekday()] == 'Sunday' or calendar.day_name[kal.weekday()] == "Saturday":
            continue
        else:
            print(kal.strftime("%Y-%m-%d"), end=' ')
            print(data["Technical Analysis: "+x][kal.strftime("%Y-%m-%d")][x])
