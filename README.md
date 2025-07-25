# Fuel Price Trends Dashboard (NSW)
Real-time interactive dashboard for visualising fuel prices across New South Wales using the [NSW FuelCheckAPI](https://api.nsw.gov.au/Product/Index/22).

Built with [Flask](https://pypi.org/project/Flask/).

## Features
- Real-time API data (NSW FuelCheck)
- Map-based visualisation
- Brand and fuel-type filters
- Clean UI with Flask

### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/aus-fuel-prices-dashboard.git
cd aus-fuel-prices-dashboard
```

### 2. Install dependencies
We recommend using a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### 3. Add your NSW FuelCheck API key
Register for a key at [https://api.nsw.gov.au/](https://api.nsw.gov.au/) and add it to a `.env` file:

```bash
FUELCHECK_API_KEY=your-api-key-here
```

(Or export it as an environment variable.)

### 4. Run the app
```bash
flask run app.py
```
---

## Future Features
- Add support for QLD, VIC, and other states
- Basic forecasting (e.g. 7-day price trends)
- Save/load custom locations and brands
- Compare brands or suburbs over time

---
## ️ Disclaimer
This app is for educational and non-commercial purposes. NSW FuelCheck API usage is subject to their terms.

---
## License
MIT License