import requests
import time

from cachetools import cached, TTLCache

url = "https://api.exchangerate-api.com/v4/latest/USD"
response = requests.get(url)
data = response.json()

ttls_cache = TTLCache(maxsize=100, ttl=3600)

base_currency = 'USD'
target_currency = 'CAD'

@cached(ttls_cache)
def exchange_rates(base_currency, target_currency):
    time.sleep(2)
    base_cr = data['rates'][base_currency]
    target_cr = data['rates'][target_currency]
    return base_cr, target_cr


if __name__ == "__main__":
    base_currency = input("Enter base currency (e.g., USD): ").upper()
    target_currency = input("Enter target currency (e.g., CAD): ").upper()
    exchange_rates(base_currency, target_currency)
    