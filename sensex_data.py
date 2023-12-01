import yfinance as yf

def get_last_sensex_value():
    # Ticker symbol for Sensex index on Yahoo Finance
    sensex_symbol = "^BSESN"

    try:
        # Fetch live data for Sensex
        sensex_data = yf.download(sensex_symbol, period="1d", interval="1m")

        # Get the last row of the data
        last_row = sensex_data.iloc[-1]

        # Print just the last value
        last_value = last_row['Close']
        print(f"Last Sensex Value: {last_value}")

    except Exception as e:
        print(f"Error fetching data: {e}")

if __name__ == "__main__":
    get_last_sensex_value()
