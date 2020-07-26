# SunsetSunriseTime
Simple Python code that outputs the local sunset and sunrise time at your location on a given date.

## Usage
- You'll need to get an API key from [Google Maps Platform](https://developers.google.com/maps/documentation/geocoding/get-api-key) to use Google's [Geocode](https://developers.google.com/maps/documentation/geocoding/start) and [Timezone](https://developers.google.com/maps/documentation/timezone/get-started) APIs.
- I used the [Sunrise-Sunset API](https://sunrise-sunset.org/api) to obtain the sunrise/sunset times for a given latitude, longitude, and date.

### Running
1. Open up a terminal and navigate to the directory the file is saved in.
2. Then call: ```python3 SunsetSunriseData.py```.
3. You'll be prompted for a location and a date.
4. Your sunrise and sunset times will be outputed in the terminal.

## How It Works
1. The user inputs a location and date. 
2. The [Geocode](https://developers.google.com/maps/documentation/geocoding/start) API translates the location to a latitude and longitude. 
3. These latitude and longitude coordinates along with the date are used to determine the sunrise/sunset times.
4. The [Timezone](https://developers.google.com/maps/documentation/timezone/get-started) API also uses latitude, longitude, and date to determine the location's timezone.
5. Finally, the times are converted from UTC to local time and outputed to the console.
