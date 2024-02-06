# (imports)
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
# ↑ Change these values according to your needs! ↑
# For example, hour is right now always the current hour, if user changes the value, override this line

# Function to format number with two digits
def two_digits(number):
    return f"0{number}" if number < 10 else str(number)

# Construct parameters
params = f"date={year}-{two_digits(month)}-{two_digits(day)}&hour={two_digits(hour)}"

# Fetch data from API
response = requests.get(f"{PRICE_ENDPOINT}?{params}")
data = response.json()

# snt/kWh
price = data['price']

# (Print for testing)
# print(f"Hinta on nyt {price}")



# Devices
## Values are in kWh
washing_mashine = 2.3


# Custom device
def own_device():
    # Ask values from the user
    custom_device = input("Oma laite ")
    consumption = input("Kulutus ")
    return custom_device, consumption
own_device()

# How long the device is in use
def time_in_use():
    # Hours asked for user comfort
    duration_hours= input("Tunnit:")
    duration_minutes = input("Minuutit:")

    #Duration converted to minutes
    duration = duration_hours*60 + duration_minutes
    return duration
time_in_use()

#kWh used

# def "Joku nimi()"
    # Laitteen nimi, joka on annettu kohdassa def own_device
    # Laitteen kulutus kokonaisuudessaan, joka on laskettu arvo kulutuksesta ja käytöstä
    # Kuinka paljon laitteen käyttö on maksanut (käytä omatekemää hinta muuttujaa kunnes API toimii)
    # Halvin hinta klo XX:XX