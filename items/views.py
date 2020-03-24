from django.shortcuts import render
import json
import urllib.request
from django.db import models


def items(request):
    return render(request, 'items.html')


# download raw json object
url = "http://ddragon.leagueoflegends.com/cdn/10.6.1/data/en_US/item.json"
data = urllib.request.urlopen(url).read().decode()

# parse json object
obj = json.loads(data)
for item in obj['data']:
    itemId = obj['data'][item]
    itemName = obj['data'][item]['name']
    itemDec = obj['data'][item]['description']
    itemText = obj['data'][item]['plaintext']
    itemImage = obj['data'][item]['image']['full']
    itemPrice = obj['data'][item]['gold']['base']
    itemSell = obj['data'][item]['gold']['sell']





class ItemTb(models.Model):
 itemIdCol = models.CharField(max_length=100)
 itemNameCol = models.CharField(max_length=100)
 itemDecCol = models.CharField(max_length=300)
 itemTextCol = models.CharField(max_length=2000)
 itemImageCol = models.IntegerField()
 itemPriceCol = models.IntegerField()
 itemSellCol = models.IntegerField()
