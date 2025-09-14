import requests

url = "https://api.exchangerate-api.com/v4/latest/USD"
response = requests.get(url)
data = response.json()

base_currency = 'USD'
target_currency = 'CAD'


def exchange_rates(base_currency, target_currency):
    base_cr = data['rates'][base_currency]
    target_cr = data['rates'][target_currency]
    return base_cr, target_cr


if __name__ == "__main__":
    base_currency = input("Enter base currency (e.g., USD): ").upper()
    target_currency = input("Enter target currency (e.g., CAD): ").upper()
    exchange_rates(base_currency, target_currency)
    