import requests
import json
from twilio.rest import Client

from PIL.ImageChops import difference

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
account_sid = "AC3e5f4e7562cf03e2b4647e980636d874"
auth_token = "435315cf27e7819a570f541aad30b8a2"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

parameter = {
  "function":"TIME_SERIES_DAILY",
  "symbol" : STOCK_NAME,
   "apikey": "B2LL7LICRQ8413KX"
}

response = requests.get(url=STOCK_ENDPOINT,params=parameter)
data = response.json()["Time Series (Daily)"]
list_data = [value for (key,value) in data.items()]
yesterday_closing_price = list_data[0]['4. close']
day_before_yesterday_closing_price = list_data[1]['4. close']
diff = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
sym=None
if diff > 5:
    sym = "🔺"
else:
    sym ="🔻"
diff_perc = round((diff / float(yesterday_closing_price)) * 100)
if abs(diff_perc) > 5:
    parameter_news = {
        "q": COMPANY_NAME,
        "apikey": "88446db964dd4b7a8bc0b56b9128dfc1",

    }

    response = requests.get(url=NEWS_ENDPOINT, params=parameter_news)
    data = response.json()['articles']
    news = data[0:3]
    news_artciles = [f"{COMPANY_NAME}: {sym}{diff_perc}% /nHeadline:{i['title']} /nBrief:{i['description']}" for i in news]
    client = Client(account_sid, auth_token)
    for i in news_artciles:
        message = client.messages \
            .create(
            body=i,
            from_="+19145065691",
            to="+919789867048"
        )

