import streamlit as st
import pandas as pd
import plotly.express as px
from fuel_api import fetch_fuel_data

st.set_page_config(page_title="NSW Fuel Price Dashboard", layout="wide")
st.title("️NSW Live Fuel Price Trends")

# Sidebar controls
st.sidebar.header("Filters")
fuel_type = st.sidebar.selectbox("Select Fuel Type", ["E10", "U91", "U95", "U98", "Diesel", "LPG"])
brand_filter = st.sidebar.text_input("Filter by Brand (optional)")

# Fetch data
data = fetch_fuel_data()

if data.empty:
    st.warning("No data available. Try again later.")
else:
    if brand_filter:
        data = data[data['brand'].str.contains(brand_filter, case=False, na=False)]

    st.subheader(f"Showing {len(data)} stations with {fuel_type} prices")

    # Show table
    st.dataframe(data[["brand", "address", "price", "last_updated"]].sort_values("price"))

    # Plot
    fig = px.scatter_mapbox(
        data,
        lat="lat",
        lon="lng",
        color="price",
        size="price",
        hover_name="brand",
        hover_data=["address", "price"],
        color_continuous_scale="Turbo",
        zoom=8,
        height=600
    )
    fig.update_layout(mapbox_style="open-street-map")
    st.plotly_chart(fig, use_container_width=True)