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
# Ask values from the user
custom_device = input("Oma laite: ")
consumption = int(input("Kulutus kWh: "))


# How long the device is in use
# Hours asked for user comfort
duration_hours=int(input("Tunnit:"))
duration_minutes = int(input("Minuutit:"))
#Duration converted to minutes
Final_duration_minutes = duration_hours*60 + duration_minutes
#Duration converted to hours
final_duration_hours= duration_hours+duration_minutes/60




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
remaining_time = Final_duration_minutes





#Price for the first active hour
current_hour_use = 60-minute
price = minuuttilaskuri()
total_price = (consumption * (current_hour_use/60))*price
remaining_time = remaining_time - (60-minute)

# Loop count (total full hours in use)
hours_in_use = int(remaining_time / 60)



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
##fix consumption after the variable
washingmachine = 0
dishwasher= 1
microwave=2
oven=3
stove=4
fridge=5
freezer=6
airfryer=7
vacuum=8
airconditionig=9
sauna=10
television=11
videogameconsole=12
laptop=13
desktopcomputer=14
sealinglamp=15
phonecharger=16
kettele=17
hairdryer=18
hairstraightner=19
dryer=20
toaster=21
coffeemaker=22


#list of selected devices 
##could make better?
devices=[washingmachine, dishwasher,microwave,oven,stove,fridge,
        freezer,airfryer,vacuum,airconditionig,sauna,
        television,videogameconsole,laptop,desktopcomputer,sealinglamp,
        phonecharger,kettele,hairdryer,hairstraightner,dryer,toaster,coffeemaker]




#kWh used on custom design
total_consumption_custom=consumption*final_duration_hours
#the price of using a custom device
custom_price=total_consumption_custom*price

#kWh used on selected devices
total_consumption_selec=devices[10]*final_duration_hours 
##on devices[] add the number of the chosen device on list
#the price of using a selected device
selected_price=total_consumption_selec*price


# custom device and selected device functions seperated:
#function for custom device
def user_custom_device():
    print(custom_device,"kuluttaa:",total_consumption_custom,"kWh")
    print(custom_device+"n käyttö maksaa",round(total_price,2),"senttiä")
user_custom_device()
#function for selected device
def user_selected_device():
    print(devices[0],"kuluttaa:",total_consumption_selec,"kWh")
    print(devices[0]+"n käyttö maksaa",selected_price,"senttiä")
user_selected_device
###prints saved for visualisation, mpdify before adding to website!!!!
