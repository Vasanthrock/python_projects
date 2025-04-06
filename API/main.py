import json
import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient


account_sid = "AC3e5f4e7562cf03e2b4647e980636d874"
auth_token = "435315cf27e7819a570f541aad30b8a2"
parameter = {
    "lat" : 9.944720,
    "lon" : 78.130783,
    "appid" : "f162ac9d7cc1e975961fd7f11b48c457",

}
response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast",params=parameter)
response.raise_for_status()
weather = response.json()
will_rain = False
for i in range(0,12):
    if weather["list"][i]["weather"][0]["id"] < 700:
        will_rain=True

if will_rain:
    # proxy_client = TwilioHttpClient()
    # proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_="+19145065691",
        to="+919789867048"
    )
    print(message.status)