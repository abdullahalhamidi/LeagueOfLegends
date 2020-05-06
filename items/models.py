from django.db import models


# Created Table with Columns
class ItemTb(models.Model):
    itemIdCol = models.CharField(max_length=100)
    itemNameCol = models.CharField(max_length=100)
    itemDecCol = models.CharField(max_length=300)
    itemTextCol = models.CharField(max_length=2000)
    itemImageCol = models.IntegerField()
    itemPriceCol = models.IntegerField()
    itemSellCol = models.IntegerField()