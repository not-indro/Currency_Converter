import streamlit as st
import requests

# Function to get currency conversion rates


def get_conversion_rate(from_currency, to_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    response = requests.get(url)
    data = response.json()
    conversion_rate = data['rates'][to_currency]
    return conversion_rate

# Function to convert currency


def convert_currency(amount, from_currency, to_currency):
    conversion_rate = get_conversion_rate(from_currency, to_currency)
    converted_amount = amount * conversion_rate
    return converted_amount


# Streamlit UI
st.set_page_config(page_title="Currency Converter App", page_icon="💱")
st.title("Currency Converter App")

currencies = requests.get(
    "https://api.exchangerate-api.com/v4/latest/USD").json()["rates"]
all_currencies = list(currencies.keys())

# Currency Converter Section
from_currency = st.selectbox("From Currency", all_currencies)
to_currency = st.selectbox("To Currency", all_currencies)
amount = st.number_input("Amount", min_value=0.01, step=0.01)

converted_amount = convert_currency(amount, from_currency, to_currency)

# Currency Converter Output
st.subheader("Currency Conversion Result")
st.header(
    f"{amount:.2f} {from_currency} is equivalent to {converted_amount:.2f} {to_currency}")
