import requests
from datetime import datetime

MY_LAT = 5.066963488771223
MY_LNG = -75.47555920016707


def is_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_longitude = float(data['iss_position']['longitude'])
    iss_latitude = float(data['iss_position']['latitude'])

    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LNG - 5 <= iss_longitude <= MY_LNG + 5:
        return True


def when_overhead():
    response = requests.get(
        url="http://api.open-notify.org/iss-pass.json?lat=5.066963488771223&lon=-75.47555920016707&alt=5321")
    response.raise_for_status()
    data_time = response.json()['response'][1]['risetime']
    time_stamp = datetime.fromtimestamp(data_time)

    # if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LNG - 5 <= iss_longitude <= MY_LNG + 5:
    #     return

    return time_stamp


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0,
    }

    response = requests.get('https://api.sunrise-sunset.org/json', params=parameters)
    data = response.json()
    sunrise = int(data['results']['sunrise'].split("T")[1].split(':')[0]) - 5
    sunset = int(data['results']['sunset'].split("T")[1].split(':')[0]) - 5
    time_now = datetime.utcnow()
    return time_now
    # if time_now.hour > sunset or time_now.hour < sunrise:
    #     return True


print(when_overhead(), "\n", is_night())
