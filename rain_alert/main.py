import requests
from twilio.rest import Client
import os

OWM_Endpoint = "PUT OWM ENDPOINT HERE"
api_key = os.environ.get("OWM_API_KEY")
account_sid = "ACf0e4e2e9d8f7f7f7f7f7f7f7f7f7f7f7"
auth_token = os.environ.get("AUTH_TOKEN")

weather_params = {
    "lat": -2.261980,
    "lon": 29.793940,
    "appid": api_key,
    "cnt": 4
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data['list']:
    condition_code = (hour_data["weather"][0]["id"])
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="It's going to rain today. Remember to  bring an umbrella",
            from_="Your Twilio number",
            to="Phone number"
        )

    print(message.status)
#
