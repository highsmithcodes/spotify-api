import requests

def get_solana_price_data():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "ids": "solana",
        "interval": "hourly",
        "range": "24h"
    }

    response = requests.get(url, params=params)
    data = response.json()

    return data

def detect_trading_patterns(price_data):
    hourly_prices = [entry['current_price'] for entry in price_data]

    # Insert your trading pattern detection logic here
    # This is just a simple example to detect an upward trend
    if hourly_prices[-1] > hourly_prices[0]:
        pattern = "Upward trend"
    else:
        pattern = "No recognizable pattern"

    return pattern

if __name__ == "__main__":
    solana_price_data = get_solana_price_data()

    if solana_price_data:
        trading_pattern = detect_trading_patterns(solana_price_data)
        print(f"Trading Pattern: {trading_pattern}")
    else:
        print("Failed to retrieve Solana price data.")
