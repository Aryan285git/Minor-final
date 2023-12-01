import yfinance as yf

def get_last_nifty_value():
    # Ticker symbol for Nifty 50 index on Yahoo Finance
    nifty_symbol = "^NSEI"

    try:
        # Fetch live data for Nifty 50
        nifty_data = yf.download(nifty_symbol, period="1d", interval="1m")

        # Get the last row of the data
        last_row = nifty_data.iloc[-1]

        # Print just the last value
        last_value = last_row['Close']
        print(f"Last Nifty Value: {last_value}")

    except Exception as e:
        print(f"Error fetching data: {e}")

if __name__ == "__main__":
    get_last_nifty_value()
