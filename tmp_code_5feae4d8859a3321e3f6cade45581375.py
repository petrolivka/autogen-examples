

def get_stock_prices(stock_symbol, start_date, end_date):
    """
    Get stock prices for a given stock symbol and date range.
    Args:
        stock_symbols (str or list): The stock symbols to get the
        prices for.
        start_date (str): The start date in the format
        'YYYY-MM-DD'.
        end_date (str): The end date in the format 'YYYY-MM-DD'.

    Returns:
        pandas.DataFrame: The stock prices for the given stock
        symbols indexed by date, with one column per stock
        symbol.
    """
    import yfinance as yf

    stock_data = yf.download(stock_symbol, start=start_date, end=end_date)
    if not stock_data:
        return None
    return stock_data.get("Close")


def plot_stock_prices(stock_prices, filename):
    """Plot the stock prices for the given stock symbols.

    Args:
        stock_prices (pandas.DataFrame): The stock prices for the
        given stock symbols.
    """
    import matplotlib.pyplot as plt

    plt.figure(figsize=(10, 5))
    for column in stock_prices.columns:
        plt.plot(stock_prices.index, stock_prices[column], label=column)
    plt.title("Stock Prices")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.savefig(filename)
    plt.close()


