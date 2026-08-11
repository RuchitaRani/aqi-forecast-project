import os
from dotenv import load_dotenv
import requests

load_dotenv()
api_key=os.getenv("OPENAQ_API_KEY")

headers={"X-API-Key": api_key}
sensor_id=14891
# url = f"https://api.openaq.org/v3/sensors/{sensor_id}/measurements"
# params = {
#      "datetime_from": "2018-03-09T00:00:00Z",
#     "datetime_to": "2018-03-16T00:00:00Z",
#     "limit": 1000
# }
# response=requests.get(url, headers=headers, params=params)
# data=response.json()
# print(response.status_code)
# print(len(data["results"]))

#print(data["results"][0]["period"]["datetimeFrom"]["local"])
#print(data["results"][-1]["period"]["datetimeFrom"]["local"])

# url_locations = "https://api.openaq.org/v3/locations/5603"
# response = requests.get(url_locations, headers=headers)
# info = response.json()
# print(info["results"][0]["datetimeFirst"])
# print(info["results"][0]["datetimeLast"])

# sensor_id = 14891
# url = f"https://api.openaq.org/v3/sensors/{sensor_id}/measurements"

# params = {
#     "datetime_from": "2025-01-01T00:00:00Z",
#     "datetime_to": "2025-02-01T00:00:00Z",
#     "limit": 1000
# }

# response = requests.get(url, headers=headers, params=params)
# data = response.json()
# print(response.status_code)
# print(len(data["results"]))

# url_sensor = "https://api.openaq.org/v3/sensors/14891"
# response = requests.get(url_sensor, headers=headers)
# info = response.json()
# print(info["results"][0]["datetimeFirst"])
# print(info["results"][0]["datetimeLast"])

# url_sensor2 = "https://api.openaq.org/v3/sensors/12234921"
# response = requests.get(url_sensor2, headers=headers)
# info = response.json()
# print(info["results"][0]["datetimeFirst"])
# print(info["results"][0]["datetimeLast"])

sensor_id = 12234921
url = f"https://api.openaq.org/v3/sensors/{sensor_id}/measurements"

params = {
    "datetime_from": "2025-02-19T00:00:00Z",
    "datetime_to": "2025-03-19T00:00:00Z",
    "limit": 1000
}

response = requests.get(url, headers=headers, params=params)
data = response.json()
print(response.status_code)
print(len(data["results"]))

first = data["results"][0]["period"]["datetimeFrom"]["local"]
last = data["results"][-1]["period"]["datetimeFrom"]["local"]
print(first, last)