import os
import requests
import pandas as pd
import datetime
import uuid
import json
from dotenv import load_dotenv

load_dotenv()

AUTH_HEADER = os.getenv("FUELCHECK_AUTH_HEADER")
API_KEY = os.getenv("FUELCHECK_API_KEY")

URL = "https://api.onegov.nsw.gov.au/FuelPriceCheck/v1/fuel/prices"

HEADERS = {
    'content-type': 'application/json; charset=utf-8',
    'authorization': AUTH_HEADER,
    'apikey': API_KEY,
    'transactionid': str(uuid.uuid4()),
    'requesttimestamp': datetime.datetime.now().isoformat() + 'Z'
}

print(HEADERS)

def fetch_fuel_data():
    try:
        response = requests.get(URL, headers=HEADERS, timeout=10)
        response.raise_for_status()
        json_data = response.json()

        records = json_data.get("stations", [])
        df = pd.DataFrame.from_records(records)

        if df.empty:
            return pd.DataFrame()

        df = df.rename(columns={
            "brand": "brand",
            "address": "address",
            "price": "price",
            "lastUpdated": "last_updated",
            "latitude": "lat",
            "longitude": "lng",
        })

        return df[["brand", "address", "price", "last_updated", "lat", "lng"]].dropna()

    except Exception as e:
        print("Error fetching fuel data:", e)
        return pd.DataFrame()
