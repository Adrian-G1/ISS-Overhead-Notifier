import requests
import datetime as dt

MY_LAT = 33.603619
MY_LONG = -101.969048


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    longitude = float(data["iss_position"]["longitude"])
    latitude = float(data["iss_position"]["latitude"])

    iss_position = (longitude, latitude)

    print(iss_position)

    # Position is within +/- 5 degrees of ISS Station
    if MY_LAT-5 <= latitude <= MY_LAT+5 and MY_LONG-5 <= longitude <= MY_LONG+5:
        return True


# # Params testing
# MY_LAT = 33.603619
# MY_LONG = -101.969048


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }
    response = requests.get(
        url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise_hr = data["results"]["sunrise"].split("T")[1].split(":")[0]
    sunset_hr = data["results"]["sunset"].split("T")[1].split(":")[0]

    time_now = dt.datetime.now().hour
    if time_now >= sunset_hr or time_now <= sunrise_hr:
        # It is dark outside
        return True


# Send email notifying ISS is overhead
