import requests
import datetime as dt

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# data = response.json()
# longitude = float(data["iss_position"]["longitude"])
# latitude = float(data["iss_position"]["latitude"])
#
# iss_position = (longitude, latitude)
#
# print(iss_position)

# Position is within +/- 5 degrees of ISS Station

# Params testing
MY_LAT = 33.603619
MY_LONG = -101.969048

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}
response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise_hr = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset_hr = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise_hr)
print(sunset_hr)

time_now = dt.datetime.now()
print(time_now.hour)
