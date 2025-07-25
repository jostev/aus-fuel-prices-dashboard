# app.py
from flask import Flask, render_template
from fuel_api import FuelChecker
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    try:
        checker = FuelChecker()
        data = checker.fetch_fuel_prices()

        records = data.get("stations", [])
        df = pd.DataFrame.from_records(records)

        if df.empty:
            return render_template("index.html", tables=[], error="No fuel data available.")

        df = df.rename(columns={
            "brand": "Brand",
            "address": "Address",
            "price": "Price",
            "lastUpdated": "Last Updated",
            "latitude": "Latitude",
            "longitude": "Longitude",
        })

        return render_template("index.html", tables=[df.to_html(classes='data', header=True, index=False)], error=None)

    except Exception as e:
        return render_template("index.html", tables=[], error=str(e))

if __name__ == '__main__':
    app.run(debug=True)
