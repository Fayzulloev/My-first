import requests
from dateutil.parser import parse 

def get_all_exchange_rates_erapi(src):
    url = f"https://open.er-api.com/v6/latest/{src}"
    # запросить открытый API ExchangeRate и преобразовать в Python dict с помощью .json()
    data = requests.get(url).json()
    if data["result"] == "success":
        # запрос выполнен успешно
        # получить последнюю обновленную дату и время
        last_updated_datetime = parse(data["time_last_update_utc"])
        # узнать курсы обмена
        exchange_rates = data["rates"]
    return last_updated_datetime, exchange_rates

def convert_currency_erapi(src, dst, amount):
    # получить все курсы обмена
    last_updated_datetime, exchange_rates = get_all_exchange_rates_erapi(src)
    # конвертировать, просто получив целевой курс обмена валюты и умножив на сумму
    return last_updated_datetime, exchange_rates[dst] * amount

if __name__ == "__main__":
    import sys
    source_currency = sys.argv[1]
    destination_currency = sys.argv[2]
    amount = float(sys.argv[3])
    last_updated_datetime, exchange_rate = convert_currency_erapi(source_currency, destination_currency, amount)
    print("Last updated datetime:", last_updated_datetime)
    print(f"{amount} {source_currency} = {exchange_rate} {destination_currency}")

