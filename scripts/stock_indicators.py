import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd
import pynance as pn

def fetch_historical_data(stocks, start_date, end_date):
    """
    Fetch historical market data for a list of stocks.
    """
    yfinance_data = []  # Initialize an empty list to store DataFrames

    for stock in stocks:
        # Fetch data for each stock
        data = pn.data.get(stock, start=start_date, end=end_date)
        yf_df = pd.DataFrame(data)  # Convert to a DataFrame
        yf_df['stock'] = stock  # Add the stock symbol to the DataFrame
        yfinance_data.append(yf_df)  # Append the DataFrame to the list

    # Concatenate all DataFrames in the list into a single DataFrame
    yfinance_df = pd.concat(yfinance_data)
    return yfinance_df


def load_data(file_path):
    """
    Load stock data from a CSV file.
    """
    df = pd.read_csv(file_path, index_col='Date', parse_dates=True)
    return df

def plot_stock_data(stock, df):
    """
    Plot stock price with moving averages.
    """
    fig, ax = plt.subplots(figsize=(14, 7))
    stock_data = df[df['stock'] == stock]
    ax.plot(stock_data.index, stock_data['Close'], label='Close Price', color='blue')
    ax.plot(stock_data.index, stock_data['SMA_20'], label='20-Day SMA', color='orange')
    ax.plot(stock_data.index, stock_data['EMA_20'], label='20-Day EMA', color='green')
    ax.set_title(f'Stock Price for {stock} with SMA and EMA')
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    ax.legend()
    ax.grid()
    return fig

def plot_rsi(stock, df):
    """
    Plot Relative Strength Index (RSI).
    """
    fig, ax = plt.subplots(figsize=(14, 5))
    stock_data = df[df['stock'] == stock]
    ax.plot(stock_data.index, stock_data['RSI_14'], label='14-Day RSI', color='purple')
    ax.axhline(70, color='red', linestyle='--', label='Overbought (70)')
    ax.axhline(30, color='green', linestyle='--', label='Oversold (30)')
    ax.set_title(f'RSI for {stock}')
    ax.set_xlabel('Date')
    ax.set_ylabel('RSI')
    ax.legend()
    ax.grid()
    return fig

def plot_macd(stock, df):
    """
    Plot MACD (Moving Average Convergence Divergence).
    """
    fig, ax = plt.subplots(figsize=(14, 7))
    stock_data = df[df['stock'] == stock]
    ax.plot(stock_data.index, stock_data['MACD'], label='MACD Line', color='black')
    ax.plot(stock_data.index, stock_data['MACD_Signal'], label='Signal Line', color='red')
    ax.bar(stock_data.index, stock_data['MACD_Hist'], label='MACD Histogram', color='gray', alpha=0.5)
    ax.set_title(f'MACD for {stock}')
    ax.set_xlabel('Date')
    ax.set_ylabel('MACD')
    ax.legend()
    ax.grid()
    return fig


