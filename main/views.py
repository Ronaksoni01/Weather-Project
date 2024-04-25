from django.shortcuts import render
import json
import urllib.request
# Create your views here.

def index(request):
    if request.method == 'POST':
        city = request.POST["city"]
    # source contain JSON data from API
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=ede3274a6ade88f3e8f4d7b39752c23d').read()
    # converting to json date to a disctionary
        list_of_data = json.loads(source)

        data = {
            "country_code":str(list_of_data["sys"]["country"]),
            "coordinate":str(list_of_data["coord"]["lon"]) + '' + str(list_of_data["coord"]["lat"]),
            "temp":str(list_of_data["main"]["temp"]) +'k',
            "humidity":str(list_of_data["main"]["humidity"]) + 'k',
            "pressure":str(list_of_data["main"]["pressure"]),  
           
        }

        print(data)
    else:
        data={ }

    return render(request,"main/index.html",data)