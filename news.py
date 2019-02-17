import requests, json

url = ('https://newsapi.org/v2/everything?'
       'q=Apple&'
       'from=2019-02-17&'
       'sortBy=popularity&'
       'apiKey=ca29302415344c19801654921781efc7')

response = requests.get(url)
return response.json()
