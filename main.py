import requests
from twilio.rest import Client
api_key = "api_key"
num = "num_virtual"
OWN_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
account_sid = "account_sid"
auth_token = "auth_token"

parameters = {
    'lat': -33.868820,
    'lon': 151.209290,
    'appid': api_key,
    'exclude': 'current,minutely,daily'
}
data = requests.get(OWN_ENDPOINT, params=parameters)
data.raise_for_status()

water_slice = data.json()["hourly"][:12]

will_rain = False

for hour_data in water_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Esta lloviendo 😥",
        from_=num,
        to='yout number phone'
    )

    print(message.status)

print(water_slice)
