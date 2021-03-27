import requests
from twilio.rest import Client

#Twilo Account information
account_sid = "ACe835130e6debbb55xxxxxxxxxx"
auth_token = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

# OpenWeatherMap 
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
params = {
    "lat": 53.11,
    "lon": 8.46,
    "exclude": "current,minutely,daily",
    "appid": "dbf7c9927b5dc5397xxxxxxxxx",
}

# Get weatherdata for the next 12 hours
response = requests.get(OWM_Endpoint, params)
response.raise_for_status()
weather_data = response.json()["hourly"]

will_rain = False
for index, entry in enumerate(weather_data[:12]):
    weather = entry["weather"]
    for condition in weather:
        # we are looking for ids < 700, thats are rainy conditions
        if condition["id"] < 700:
            will_rain = True

if will_rain:
    # when we found rain, send a message over twilio
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Es wird heute regnen ☔",
        from_='+1xxxxxxxxxxx',
        to='+49xxxxxxxxxxx'
    )
