# filename: plot_stock_gains.py
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

def fetch_and_plot_stocks(stocks, start_date, end_date, output_file):
    # Fetch stock data
    data = yf.download(stocks, start=start_date, end=end_date)
    # Calculate YTD gain as percentage from the first day of the year
    ytd_gains = (data['Close'] / data['Close'].iloc[0] - 1) * 100
    
    # Plotting
    plt.figure(figsize=(10, 6))
    for stock in stocks:
        plt.plot(ytd_gains[stock], label=f'{stock} YTD Gain (%)')
    plt.title('YTD Stock Gains for NVDA and TSLA in 2025')
    plt.xlabel('Date')
    plt.ylabel('Gain (%)')
    plt.legend()
    plt.grid(True)
    plt.savefig(output_file)
    plt.close()

# Define stock symbols, dates, and output file name
stocks = ['NVDA', 'TSLA']
start_date = '2025-01-01'
end_date = '2025-01-27'
output_file = 'ydt_stock_gains.png'

# Call the function
fetch_and_plot_stocks(stocks, start_date, end_date, output_file)

print("Plot saved successfully as 'ydt_stock_gains.png'.")