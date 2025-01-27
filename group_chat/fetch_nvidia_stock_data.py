# filename: fetch_nvidia_stock_data.py

import yfinance as yf
from datetime import datetime, timedelta

# Set the ticker symbol and the date range
ticker_symbol = "NVDA"
end_date = datetime.today().date()
start_date = end_date - timedelta(days=30)

# Retrieve historical data
data = yf.download(ticker_symbol, start=start_date, end=end_date)

# Display the first few rows of the data
print(data.head())