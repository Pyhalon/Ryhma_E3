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
# ↑ Change these values according to your needs! ↑
# For example, hour is right now always the current hour, if user changes the value, override this line

# Custom device
# Ask values from the user only used when machine not in device list:
custom_device = input("Oma laite: ")
consumption = float(input("Kulutus kWh: "))


# How long the device is in use
# Hours asked for user comfort
duration_hours=int(input("Tunnit:"))
duration_minutes = int(input("Minuutit:"))
#Duration converted to minutes
final_duration_minutes = duration_hours*60 + duration_minutes
#Duration converted to hours
final_duration_hours= duration_hours+duration_minutes/60


if 24 - date_and_time_now.hour < duration_hours and date_and_time_now.hour < 14:
    print("Sähkön hintoja ei vielä tiedossa huomiselle")
    quit()



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



#Converting the time in use to a function that is safe to play around with
remaining_time = final_duration_minutes


#Price for the first active hour
current_hour_use = 60-minute
price = minuuttilaskuri()
total_price = (consumption * (current_hour_use/60))*price
remaining_time = remaining_time - (60-minute)

# Loop count (total full hours in use)
hours_in_use = int(remaining_time / 60)

#price of the whole active hours
for i in range(hours_in_use):
    hour = hour + 1
    price = minuuttilaskuri()
    total_price = total_price + consumption * price

    if hour == 24:
        hour = 00
        day = day + 1
# Hajoaa kuukauden viimeisenä päivänä :)
           

#Remaining minutes during the last hour
remaining_time = remaining_time - (hours_in_use*60)
hour = hour + 1
price = minuuttilaskuri()
total_price = total_price + price*(consumption * (remaining_time/60))


#selected devices and their assigned consumptions
#consumption in kW/h
washingmachine = 1.7
dishwasher= 1.8
microwave= 1
oven=1.2
inductionstove=2.6
fridgefreezer=0.05
vacuum=0.7
airconditioning=1.1
sauna=5
television=0.16
videogameconsole=0.15
desktopcomputer=0.3
LEDlamp=0.005
phonecharger=0.08
kettle=1.2
hairdryer=1.5
ironingboard=2
dryer=1
toaster=1.2
coffeemaker=0.6


#list of selected devices 
##could make better?
#Made so frontend can use in a list
devices=[washingmachine, dishwasher,microwave,oven,inductionstove,fridgefreezer,
        vacuum,airconditioning,sauna,
        television,videogameconsole,desktopcomputer,LEDlamp,
        phonecharger,kettle,hairdryer,ironingboard,dryer,toaster,coffeemaker]


#kWh used on custom design
total_consumption_custom=consumption*final_duration_hours

#kWh used on selected devices
total_consumption_selec=devices[2]*final_duration_hours 
##on devices[] add the number of the chosen device on list
#the price of using a selected device
selected_price=total_consumption_selec*price


# custom device and selected device functions seperated:
#function for custom device
#total_price means the final price of a custom device. 
#selected_price means the final price of a machine on out list. 
def user_custom_device():
    print(custom_device,"kuluttaa:",total_consumption_custom,"kWh") #is this needed for the website?
    print(custom_device+"n käyttö maksaa",round(total_price,2),"senttiä")
user_custom_device()
#function for selected device
def user_selected_device():
    print(devices[0],"kuluttaa:",total_consumption_selec,"kWh")
    print(devices[0]+"n käyttö maksaa",selected_price,"senttiä")
user_selected_device
###prints saved for visualisation, mpdify before adding to website!!!!