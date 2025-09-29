import requests
import datetime

def get_eth_price():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {"ids": "ethereum", "vs_currencies": "usd"}
    response = requests.get(url, params=params)
    data = response.json()
    return data["ethereum"]["usd"]

if __name__ == "__main__":
    price = get_eth_price()
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{now}] ETH Price: ${price}")
  
