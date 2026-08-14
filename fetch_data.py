import os
from dotenv import load_dotenv
import requests
import time
load_dotenv()

api_key=os.getenv("OPENAQ_API_KEY")
headers={"X-API-KEY": api_key}

def fetch_all_measurements(sensor_id, datetime_from, datetime_to):
    url=f"https://api.openaq.org/v3/sensors/{sensor_id}/measurements"
    all_results=[]
    current_from=datetime_from

    while True:
        params={
            "datetime_from": current_from,
            "datetime_to": datetime_to,
            "limit": 1000
        }

        response=requests.get(url, headers=headers, params=params)
        data=response.json()
        results=data["results"]

        if len(results)==0:
            break

        all_results.extend(results)

        current_from = results[-1]["period"]["datetimeTo"]["utc"]
        if len(results)<1000:
            break

        time.sleep(0.2)

    return all_results

if __name__ == "__main__":
    import pandas as pd

    sensor_id = 12234921
    results = fetch_all_measurements(
        sensor_id,
        "2025-05-01T00:00:00Z",
        "2025-08-01T00:00:00Z"
    )
    print(len(results))

    cleaned = []
    for r in results:
        cleaned.append({
            "datetime_utc": r["period"]["datetimeFrom"]["utc"],
            "pm25": r["value"]
        })

    df = pd.DataFrame(cleaned)
    df.to_csv("data/pm25_raw.csv", index=False)
    print("Saved to data/pm25_raw.csv")
