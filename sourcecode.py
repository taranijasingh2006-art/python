from requests import get
from pprint import PrettyPrinter

# The original free API is no longer working.
# For demonstration purposes, we will use mock data.
# BASE_URL = "https://free.currconv.com/"
# API_KEY = "562ddaf40c95f5d58108"

printer = PrettyPrinter()


def get_currencies():
    print("Using mock currency data due to API unavailability.")
    mock_data = {
        "USD": {"currencyName": "United States Dollar", "id": "USD", "currencySymbol": "$"},
        "EUR": {"currencyName": "Euro", "id": "EUR", "currencySymbol": "€"},
        "GBP": {"currencyName": "British Pound", "id": "GBP", "currencySymbol": "£"},
        "JPY": {"currencyName": "Japanese Yen", "id": "JPY", "currencySymbol": "¥"}
    }

    data = list(mock_data.items())
    data.sort()
    return data


def print_currencies(currencies):
    if not currencies:
        print("No currencies to display.")
        return
    for _id, currency_info in currencies:
        name = currency_info['currencyName']
        symbol = currency_info.get("currencySymbol", "")
        print(f"{_id} - {name} - {symbol}")


def exchange_rate(currency1, currency2):
    print(f"Using mock exchange rate for {currency1} to {currency2}.")

    mock_rates = {
        "USD_EUR": 0.92,
        "EUR_USD": 1.08,
        "USD_GBP": 0.79,
        "GBP_USD": 1.27,
        "USD_JPY": 155.0,
        "JPY_USD": 0.0064,
        "EUR_GBP": 0.86,
        "GBP_EUR": 1.16,
        "EUR_JPY": 168.0,
        "JPY_EUR": 0.0060,
        "GBP_JPY": 195.0,
        "JPY_GBP": 0.0051,
        "USD_INR": 89.61,
        "INR_USD": 0.0112
    }

    key = f"{currency1}_{currency2}"
    rate = mock_rates.get(key)

    if rate is None:
        print(f"Mock rate not available for {currency1} -> {currency2}. Returning 1.0 for demonstration.")
        return 1.0

    print(f"{currency1} -> {currency2} = {rate}")
    return rate


def convert(currency1, currency2, amount):
    rate = exchange_rate(currency1, currency2)
    if rate is None:
        return

    try:
        amount = float(amount)
    except:
        print("Invalid amount.")
        return

    converted_amount = rate * amount
    print(f"{amount} {currency1} is equal to {converted_amount} {currency2}")
    return converted_amount


def main():
    currencies = get_currencies()

    print("Welcome to the currency converter!")
    print("List - lists the different currencies")
    print("Convert - convert from one currency to another")
    print("Rate - get the exchange rate of two currencies")
    print()

    while True:
        try:
            command = input("Enter a command: ").lower()
        except EOFError:
            print(" Exiting.")
            break

        if command == "q":
            break
        elif command == "list":
            print_currencies(currencies)
        elif command == "convert":
            currency1 = input("Enter a base currency : ").upper()
            amount = input(f"Enter an amount in {currency1}: ")
            currency2 = input("Enter a currency to convert to: ").upper()
            convert(currency1, currency2, amount)
        elif command == "rate":
            currency1 = input("Enter a base currency : ").upper()
            currency2 = input("Enter a currency to convert to : ").upper()
            exchange_rate(currency1, currency2)
        else:
            print("Unrecognized-command!")

main()
