import os
import pandas as pd
import datetime
import uuid
import json
import http.client
from dotenv import load_dotenv

load_dotenv()

AUTH_HEADER = os.getenv("FUELCHECK_AUTH_HEADER")
API_KEY = os.getenv("FUELCHECK_API_KEY")

URL = "https://api.onegov.nsw.gov.au/"

class FuelChecker:
    BASE_HOST = "api.onegov.nsw.gov.au"
    TOKEN_URL = "/oauth/client_credential/accesstoken?grant_type=client_credentials"
    PRICES_URL = "/FuelPriceCheck/v1/fuel/prices"
    LOCATION_URL = "/FuelPriceCheck/v1/fuel/locations"

    def __init__(self):
        self.conn = http.client.HTTPSConnection(self.BASE_HOST)
        
        self.access_token = self.get_access_token()
        self.headers = {
            'content-type': 'application/json; charset=utf-8',
            'authorization': f"Bearer {self.access_token}",
            'apikey': API_KEY,
            'transactionid': str(uuid.uuid4()),
            'requesttimestamp': datetime.datetime.now().isoformat() + 'Z'
        }

    def get_access_token(self):
        headers = {
            'content-type': "application/json",
            'authorization': AUTH_HEADER
        }
        self.conn.request("GET", self.TOKEN_URL, headers=headers)
        res = self.conn.getresponse()
        if res.status != 200:
            raise Exception(f"Failed to obtain access token: {res.status} {res.reason}")
        data = res.read()
        token_data = json.loads(data.decode("utf-8"))
        return token_data.get("access_token")
    
    def fetch_fuel_prices(self):
        self.conn.request("GET", self.PRICES_URL, headers=self.headers)
        res = self.conn.getresponse()
        if res.status != 200:
            raise Exception(f"Failed to fetch fuel prices: {res.status} {res.reason}")
        data = res.read()
        return json.loads(data.decode("utf-8"))
    