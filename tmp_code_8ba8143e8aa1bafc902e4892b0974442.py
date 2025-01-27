from functions import get_stock_prices, plot_stock_prices

# Define the stock symbols and the date range (start of the year 2025 to today)
stock_symbols = ['NVDA', 'TSLA']
start_date = '2025-01-01'
end_date = '2025-01-27'  # Today's date as specified

# Get the stock prices using the provided user defined function
stock_prices = get_stock_prices(stock_symbols, start_date, end_date)

# Calculate the Year-To-Date (YTD) gains by comparing the latest price to the first price of the year
ytd_gains = stock_prices.ffill().iloc[-1] / stock_prices.ffill().iloc[0] - 1
ytd_gains.index.name = 'Stock Symbol'
ytd_gains.name = 'YDT Gain'

# Plotting the YDT gains for NVDA and TSLA
fig, ax = plt.subplots()
ytd_gains.plot(kind='bar', color=['#1f77b4', '#ff7f0e'])
ax.set_title('YDT Gains for NVDA and TSLA')
ax.set_ylabel('Gain')
ax.set_xlabel('Stock Symbol')
ax.yaxis.set_major_formatter(mtick.PercentFormatter(1.0))
plt.tight_layout()

# Save the figure
plt.savefig('ydt_stock_gains.png')

# Display the plot
plt.show()