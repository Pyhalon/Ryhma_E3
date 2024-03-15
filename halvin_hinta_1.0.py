import requests
from datetime import datetime

# API / Scrape
PRICE_ENDPOINT = 'https://api.porssisahko.net/v1/price.json'

# Get current date and time
date_and_time_now = datetime.now()
year = date_and_time_now.year
month = date_and_time_now.month
day = date_and_time_now.day
hour = date_and_time_now.hour
minute = date_and_time_now.minute

def minuuttilaskuri():
    def two_digits(number):
        return f"0{number}" if number < 10 else str(number)

    # Construct parameters
    params = f"date={year}-{two_digits(month)}-{two_digits(day)}&hour={two_digits(hour)}"

    # Fetch data from API
    response = requests.get(f"{PRICE_ENDPOINT}?{params}")
    data = response.json()

    # snt/kWh
    price = data['price']

    return(price)


halvin_hinta = minuuttilaskuri()

for i in range(24-date_and_time_now.hour):
    hour = hour + 1
    check_price = minuuttilaskuri()
    if check_price < halvin_hinta:
        halvin_hinta = check_price
        when = hour

print("Halvin hinta tänään on", halvin_hinta, "kello", when+".")


if date_and_time_now.hour > 14:
    day = day + 1
    hour = 00
    halvin_hinta_tmr = minuuttilaskuri
    for i in range(24):
        hour = hour + 1
        check_price_tmr = minuuttilaskuri()
        if check_price_tmr < halvin_hinta_tmr:
            halvin_hinta_tmr = check_price_tmr
            when_tmr = hour
    print("Halvin hinta huomenna on", halvin_hinta_tmr, "kello", when_tmr,".")
else:
    print("Huomisen hinnat tiedossa kello 14.00 jälkeen.")

