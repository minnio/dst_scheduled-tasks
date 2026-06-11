import requests
from twilio.rest import Client
import os

tel = os.environ.get("TEL")
api_key = os.environ.get("OWM_API_KEY")
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")

client = Client(account_sid, auth_token)

api_param = {
    "lat":50.064651,
    "lon":19.944981,
    "appid": api_key,
    "units": "metric",
    "cnt": 4
}
response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=api_param)
response.raise_for_status()
print(f"resp code: {response.status_code}")
data = response.json()

ids = [measure["weather"][0]["id"] for measure in data["list"]]

is_rain = [True if i<800 else False for i in ids]

if True in is_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="It is going to rain",
        from_="+1 276 246 2938",
        to="tel",
    )
    print(message.status)
