import requests
from datetime import datetime
 
# API / Scrape
PRICE_ENDPOINT = 'https://api.porssisahko.net/v1/price.json'

combined_minutes = 90

# Get current date and time
date_and_time_now = datetime.now()
year = date_and_time_now.year
month = date_and_time_now.month
day = date_and_time_now.day
hour = date_and_time_now.hour
minute = date_and_time_now.minute

def two_digits(number):
    return f"0{number}" if number < 10 else str(number)


# Construct parameters
params = f"date={year}-{two_digits(month)}-{two_digits(day)}&hour={two_digits(hour)}"

# Fetch data from API
response = requests.get(f"{PRICE_ENDPOINT}?{params}")
data = response.json()

# snt/kWh
price = data['price']



#Converting the time in use to a function that is safe to play around with
remaining_time = combined_minutes

#Time in use during the current hour
remaining_time = remaining_time - (60 - minute)
current_hour_use = price*remaining_time

# Loop count (total full hours in use)
hours_in_use = int(remaining_time / 60)

#for i in range(hours_in_use):
    

#Remaining minutes during the last hour
remaining_time = remaining_time - (hours_in_use*60)
print(remaining_time)

#while remaining_time > 0:
#    if remaining_time > 60-minute:
#        remaining_time = remaining_time - minute
#        hour = date_and_time_now.hour + 1
#        if remaining_time > 60:
