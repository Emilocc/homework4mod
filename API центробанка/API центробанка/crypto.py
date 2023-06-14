# import requests
#
#
# def get_price(crypto):
#     url = "https://api.coincap.io/v2/assets/"
#     headers = {
#         "Accepts": "application/json",
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) "
#                       "Chrome/58.0.3029.110 Safari/537.36",
#     }
#     response = requests.get(url + crypto, headers=headers)
#     data = response.json()
#
#     price = data["data"]["priceUsd"]
#     name = data["data"]["name"]
#     symbol = data["data"]["symbol"]
#
#     print(f"{name} ({symbol}) current market price is: ${price}")
#
#
# choice = input("Текущую цену на какую криптовалюту вы бы хотели видеть? (BTC, ETH, XRP): ").upper()
#
# if choice == "BTC":
#     get_price("bitcoin")
# elif choice == "ETH":
#     get_price("ethereum")
# elif choice == "XRP":
#     get_price("xrp")
# else:
#     print("Invalid choice. Please enter either BTC, ETH, or XRP.")

import requests


def get_price(crypto):
    url = "https://api.coincap.io/v2/assets/"
    headers = {
        "Accepts": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/58.0.3029.110 Safari/537.36",
    }
    response = requests.get(url + crypto, headers=headers)
    data = response.json()

    price = data["data"]["priceUsd"]
    return price


choice = input("Текущую цену на какую криптовалюту вы бы хотели видеть? (BTC, ETH, XRP): ").upper()

if choice == "BTC":
    bitcoin_price = get_price("bitcoin")
    print(f"Bitcoin current market price is: ${bitcoin_price}")
elif choice == "ETH":
    ethereum_price = get_price("ethereum")
    print(f"Ethereum current market price is: ${ethereum_price}")
elif choice == "XRP":
    xrp_price = get_price("xrp")
    print(f"XRP current market price is: ${xrp_price}")
else:
    print("Invalid choice. Please enter either BTC, ETH, or XRP.")
