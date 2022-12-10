# Python module to clima
import requests
import os
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()
class  clima: 
    icon = {
        '01d': '☀️',
        '01n': '🌙',
        '02d': '🌤',
        '02n': '🌙🌤',
        '03d': '🌥',
        '03n': '🌙🌥',
        '04d': '☁☁',
        '04n': '🌙☁☁',
        '09d': '🌧',
        '09n': '🌧',
        '10d': "🌦",
        '10n': "🌙🌦",
        '11d': "⛈",
        '11n': "🌙⛈",
        '13d': "🌨"
    }
    def __init__(self) :
       self.complete_url = os.getenv('BASE_URL')+os.getenv('API_KEY')
        
    def mostrar(self):
        try:
            response = requests.get(self.complete_url)
            clima = response.json()
            current_temperature = "temperatura: " + str(clima["main"]["temp"])+"°C \n\n humedad: "+str(
                clima["main"]["humidity"])+"% \n\n clima: "+str(clima["weather"][0]["description"]+" "+self.icon[clima["weather"][0]["icon"]])
            
            return current_temperature
        except Exception as e:
            print("hay un error consultando el clima" + repr(e))
