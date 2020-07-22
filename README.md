# SunsetSunriseTime
A simple Python script that outputs the local sunset and sunrise time at your location at a given time.

## Usage
- You'll need to get an API key from [Google Maps Platform](https://developers.google.com/maps/documentation/geocoding/get-api-key) to use the [Geocode](https://developers.google.com/maps/documentation/geocoding/start) and [Timezone](https://developers.google.com/maps/documentation/timezone/get-started) APIs from Google.
- I used [Sunrise-Sunset API](https://sunrise-sunset.org/api) to obtain the sunrise/sunset times for a given latitude, longitude, and date.

## How It Works
1. The user inputs a location and date. 
2. The [Geocode](https://developers.google.com/maps/documentation/geocoding/start) API translates the location to a latitude and longitude. 
3. These latitude and longitude coordinates along with the date are used to determine the sunrise/sunset times.
4. The [Timezone](https://developers.google.com/maps/documentation/timezone/get-started) API also uses latitude, longitude, and date to determine the location's timezone.
5. Finally, the times are converted from UTC to local time and outputed to the console.
