import requests
import json
#pulls weather conditions from open weather map
def retrieve_weather(location):
    try:
        location = location.replace('!weather ', '')
        if len(location) == 0:
            location = '47906'
        payload = {
            'zip' : '47906',
            'units' : 'imperial',
            'APPID' : 'f95d01fd26ff7a19e342a0621bd1fd93'

        }
        weather = requests.get("http://api.openweathermap.org/data/2.5/weather", params=payload)
        response = weather.json()
        print(response)
        temp = response['main']['temp']
        wind = response['wind']['speed']
        wind_direction = degToCompass(int(response['wind']['deg']))

        sky = response['weather'][0]['main']
        return_string = "Current conditions\n temp: {}, wind: {} {}, sky: {}".format(temp, wind, wind_direction, sky)
        return return_string
    except:
        return "Cannot retrieve weather at this time"


#converts direction from degrees to cardinal direction
def degToCompass(num):
    val=int((num/22.5)+.5)
    arr=["N","NNE","NE","ENE","E","ESE", "SE", "SSE","S","SSW","SW","WSW","W","WNW","NW","NNW"]
    return (arr[(val % 16)])
