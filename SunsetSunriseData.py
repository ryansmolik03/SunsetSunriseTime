import requests
import json
import time
import calendar

from datetime import datetime
from datetime import date
from dateutil import tz

GEOCODE_API_KEY = ""
geocode_url = "https://maps.googleapis.com/maps/api/geocode/json?address="
sunrise_url = "https://api.sunrise-sunset.org/json"
timezone_url = "https://maps.googleapis.com/maps/api/timezone/json?location="

months = ["", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

# gets the json response from the Google Geocode API based on the inputted address
def getLocationCoordinates(address):
    address = address.replace(" ", "+")
    url = geocode_url + address + "&key=" + GEOCODE_API_KEY
    response = requests.get(url).json()

    return response if response["status"] == "OK" else None

# gets the sunrise/sunset API json response based on the latitude and longitude of the address
def getSunriseSunsetData(lat, lng, date):
    url = sunrise_url + "?lat=" + str(lat) + "&lng=" + str(lng) + "&date=" + str(date) + "&formatted=0"
    response = requests.get(url).json()

    return response if response["status"] == "OK" else None

# gets the json response from the Google TimeZone API based on the inputted location and date
def getTimezoneData(lat, lng, date):
    # get time stamp
    ts = calendar.timegm(time.strptime(date, '%Y-%m-%d'))
    
    url = timezone_url + str(lat) + "," + str(lng) + "&timestamp=" + str(ts) + "&key=" + GEOCODE_API_KEY
    response = requests.get(url).json()
    
    return response if response["status"] == "OK" else None

# prints a formatted output for the sunrise/sunset at the given location
def printResults(response, address, tz_id, lat, lng):
    sunriseArr = str(convertToLocalTime(response["results"]["sunrise"], lat, lng, tz_id)).split(" ")
    sunsetArr  = str(convertToLocalTime(response["results"]["sunset"], lat, lng, tz_id)).split(" ")

    date = sunriseArr[0].split("-")
    sunriseTime = sunriseArr[1].split("-")[0]
    sunsetTime = sunsetArr[1].split("-")[0]

    if "+" in sunriseTime:
        sunriseTime = sunriseTime.split("+")[0]
    
    if "+" in sunsetTime:
        sunsetTime = sunsetTime.split("+")[0]

    print("On: " + months[int(date[1])] + " " + date[2] + ", " + date[0])
    print("At: " + address)
    print("Sunrise: " + str(sunriseTime) + "\nSunset: " + str(sunsetTime))

def convertToLocalTime(dateTimeStr, lat, lng, tz_id):
    dateStr = dateTimeStr.replace("T", " ")
    utcStr = dateStr.split("+")[0]

    from_zone = tz.tzutc()
    to_zone = tz.gettz(tz_id)
    
    utc = datetime.strptime(utcStr, '%Y-%m-%d %H:%M:%S')
    utc = utc.replace(tzinfo=from_zone)

    local = utc.astimezone(to_zone)

    return local

if __name__ == "__main__":
    # input string address
    address = str(input("Enter Address: "))
    # input string date or today
    input_date = str(input("Enter date (2020-04-01 or today): "))

    # reformat the input_string to current date if today is inputted
    if input_date == 'today' or input_date == '':
        input_date = date.today()
        input_date = str(input_date)

    # obtain the geocode location response
    locationResponse = getLocationCoordinates(address)

    # check if the location response was returned properly
    if locationResponse != None:
        # obtain latitude, longitude, and formatted address information
        lat = locationResponse["results"][0]["geometry"]["location"]["lat"]
        lng = locationResponse["results"][0]["geometry"]["location"]["lng"]
        formatted_address = locationResponse["results"][0]["formatted_address"]

        # obtain the sunrise/sunset response
        dataResponse = getSunriseSunsetData(lat, lng, input_date)
        
        # check if the sunrise/sunset response was returned properly
        if dataResponse != None:
            # obtain the time zone response
            tzResponse = getTimezoneData(lat, lng, input_date)
            
            # check if the time zone response was returned properly
            if tzResponse != None:
                # obtain the time zone id
                tz_id = tzResponse["timeZoneId"]
                # print the address, date, and sunrise/sunset
                printResults(dataResponse, formatted_address, tz_id, lat, lng)
            else:
                print("Invalid Location")
        else:
            print("Invalid Location")
    else:
        print("Invalid Location")