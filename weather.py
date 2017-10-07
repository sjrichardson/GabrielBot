import requests
import json
import os
#pulls weather conditions from open weather map
def retrieve_weather(location):
    try:
        location = location.replace('!weather ', ' ')
        print(loc)
        if location.isspace():
            location = '47906'
        print(location)
        payload = {
            'zip' : location.strip(),
            'units' : 'imperial',
            'APPID' : os.getenv('WEATHER_KEY')

        }
        weather = requests.get(os.getenv('WEATHER_URL'), params=payload)
        response = weather.json()
        print(response)
        temp = response['main']['temp']
        wind = response['wind']['speed']
        wind_direction = degToCompass(int(response['wind']['deg']))

        sky = response['weather'][0]['main']
        return_string = "Current conditions\ntemp: {}F, wind: {}MPH {}, sky: {}".format(temp, wind, wind_direction, sky)
        return return_string
    except:
        return "Cannot retrieve weather at this time"


#converts direction from degrees to cardinal direction
def degToCompass(num):
    val=int((num/22.5)+.5)
    arr=["N","NNE","NE","ENE","E","ESE", "SE", "SSE","S","SSW","SW","WSW","W","WNW","NW","NNW"]
    return (arr[(val % 16)])
