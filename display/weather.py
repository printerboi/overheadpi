from inky.auto import auto
from PIL import Image, ImageDraw, ImageFont
from dotenv import load_dotenv
import requests
import os

load_dotenv()
lat = os.getenv('LAT')
lon = os.getenv('LON')
apikey = os.getenv('APIKEY')

def getWeatherImage(Id):
    imageName = ""

    #Thunderstorm
    if Id < 300:
        imageName = "thunder.png"
    #drizzle
    elif Id >= 300 and Id < 500:
        imageName = "drizzle.png"
    #rain
    elif Id >= 500 and Id < 600:
        imageName = "rain.png"
    #snow
    elif Id >= 600 and Id < 700:
        imageName = "snow.png"
    #fog
    elif Id >= 700 and Id < 800:
        imageName = "fog.png"
    #clear
    elif Id == 800:
        imageName = "clear.png"
    #clouds
    else:
        imageName = "cloud.png"

    return imageName
    

def kelvinToCelsius(tempInKelv):
    return round(tempInKelv - 273.15, 2)

def getWeatherData():
    response = requests.get("https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}".format(lat, lon, apikey))
    if response.status_code == 200:
        return response.json()
    else:
        return null

def loadWeather():
    weatherData = getWeatherData()
    if weatherData:
        wId = weatherData["weather"][0]["id"]
        wState = weatherData["weather"][0]["main"]
        temp = weatherData["main"]["temp"]

        display = auto()

        out = Image.new('P', (250, 122), display.WHITE)
        logo = Image.open('ressources/icons/{}'.format(getWeatherImage(wId)))

        fnt =  ImageFont.truetype("Roboto.ttf", 22)
        d = ImageDraw.Draw(out)

        d.text((90, 20), wState, display.BLACK, font=fnt)
        fnt =  ImageFont.truetype("Roboto.ttf", 14)
        d.text((91, 44), "temp: {} °C".format(kelvinToCelsius(temp)), display.BLACK, font=fnt)

        out.paste(logo, (0, 0))

        display.set_image(out)
        display.show()

    

