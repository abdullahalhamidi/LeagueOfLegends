from django.db import models


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