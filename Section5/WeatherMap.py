import requests

city = 'chicago'
            #the library we are getting infor from                            added city varaible where city name goes for more accurate and easy change                             
url = 'http://api.weatherapi.com/v1/current.json?key=a8d837fc27604902a46195239251205&q=' + city + '&aqi=no'
response = requests.get(url)
weather_json = response.json() #parses json 

            #currentkey then chain temp_f for fahrenheit temp
temp = weather_json.get('current').get('temp_f')
            # Gets condition of the weather 
description = weather_json.get('current').get('condition').get('text')



print("Todays weather in ", city, 'is', description, temp)