from django.shortcuts import render
import json
import urllib.request
from django.db import models


# Download raw json object
url = "http://ddragon.leagueoflegends.com/cdn/10.6.1/data/en_US/champion.json"
data = urllib.request.urlopen(url).read().decode()

# Parse json object
obj = json.loads(data)

# Access json elements
try:
 for id in obj['data']:
  title = obj['data'][id]['id']
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
except Exception as problem:
    print("An error has occured" + type(problem), problem.args)


# Created Table with Columns
class ChampionsTb(models.Model):
 idCol = models.CharField(max_length=100)
 nameCol = models.CharField(max_length=100)
 titleCol = models.CharField(max_length=300)
 blurbCol = models.CharField(max_length=2000)
 attackCol = models.IntegerField()
 defenseCol = models.IntegerField()
 magicCol = models.IntegerField()
 difficultyCol = models.IntegerField()
 imageCol = models.CharField(max_length=200)
 hpCol = models.FloatField()
 movespeedCol = models.FloatField()
 armorCol = models.FloatField()
 attackrangeCol = models.FloatField()
 hpregenCol = models.FloatField()
 attackdamageCol = models.FloatField()
 attackspeedCol = models.FloatField()


# Render out content
def champions(request):
    return render(request, 'champions.html')