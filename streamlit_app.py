import pandas as pd
import streamlit as st
import yfinance as yf


btc=yf.download("BTC-USD","2008-01-01","2023-08-12")
st.table(btc)
