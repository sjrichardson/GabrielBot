import requests
#pulls weather conditions from open weather map
def retrieve_weather(location):
    location = location.replace('!weather ', '')
    if len(location) == 0:
        location = '47906'
    weather = requests.get("api.openweathermap.org/data/2.5/weather", params=location)
    response = weather.json()

    temp = response['main']['temp']
    wind = response['main']['wind']['speed']
    wind_direction = degToCompass(response['main']['wind']['deg'])

    sky = response['weather'][0]['main']
    return_string = "Current conditions\n temp: {}, wind: {}{}, sky: {}".format(temp, wind, wind_direction, sky)

    return return_string

#converts direction from degrees to cardinal direction
def degToCompass(num):
    val=int((num/22.5)+.5)
    arr=["N","NNE","NE","ENE","E","ESE", "SE", "SSE","S","SSW","SW","WSW","W","WNW","NW","NNW"]
    print (arr[(val % 16)])
