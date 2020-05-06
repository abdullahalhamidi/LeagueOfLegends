from django.shortcuts import render
import json
import urllib.request
from django.http import HttpResponse


# Download raw json objects
url = "http://ddragon.leagueoflegends.com/cdn/10.6.1/data/en_US/item.json"
data = urllib.request.urlopen(url).read().decode()

# Parse json object
obj = json.loads(data)

# Access json elements
for item in obj['data']:
    itemId = obj['data'][item]
    itemName = obj['data'][item]['name']
    itemDec = obj['data'][item]['description']
    itemText = obj['data'][item]['plaintext']
    itemImage = obj['data'][item]['image']['full']
    itemPrice = obj['data'][item]['gold']['base']
    itemSell = obj['data'][item]['gold']['sell']


# Render out content
def items(request):
    return render(request, 'items.html')