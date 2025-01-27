# filename: analyze_nvidia_stock_data.py

import pandas as pd
from fetch_nvidia_stock_data import data

# Calculate the relevant metrics
opening_price = data.iloc[0]['Open']    # Opening price at start of the month
closing_price = data.iloc[-1]['Close']  # Closing price at end of the month
highest_price = data['High'].max()      # Highest price of the month
lowest_price = data['Low'].min()        # Lowest price of the month
percentage_change = ((closing_price - opening_price) / opening_price) * 100

# Print the results
print(f"Opening Price: {opening_price}")
print(f"Closing Price: {closing_price}")
print(f"Highest Price: {highest_price}")
print(f"Lowest Price: {lowest_price}")
print(f"Percentage Change: {percentage_change:.2f}%")