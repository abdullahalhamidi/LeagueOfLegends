from django.shortcuts import render
from django.http import HttpResponse
import json
import urllib.request

def champions(request):
    return render(request, 'champions.html')

# download raw json object
url = "http://ddragon.leagueoflegends.com/cdn/10.6.1/data/en_US/champion.json"
data = urllib.request.urlopen(url).read().decode()

# parse json object
obj = json.loads(data)
try:
    for name in obj['data']:
     name = obj['data'][id]['name']
     title = obj['data'][id]['title']
     blurb =  obj['data'][id]['blurb']
     attack = obj['data'][id]['info']['attack']
     defense = obj['data'][id]['info']['defense']
     magic = obj['data'][id]['info']['magic']
     difficulty = obj['data'][id]['info']['difficulty']
     image = obj['data'][id]['image']['full']
     hp = obj['data'][id]['stats']['hp']
     movespeed = obj['data'][id]['stats']['movespeed']
     armor =  obj['data'][id]['stats']['armor']
     attackrange = obj['data'][id]['stats']['attackrange']
     hpregen = obj['data'][id]['stats']['hpregen']
     attackdamage = obj['data'][id]['stats']['attackdamage']
     attackspeed = obj['data'][id]['stats']['attackspeed']
except:
    print("error")