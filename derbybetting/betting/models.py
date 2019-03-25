from django.db import models

class People(models.Model):
    name = models.CharField(max_length=200,null=False)

class Horse(models.Model):
    name = models.CharField(max_length=200,null=False)
    jockey = models.CharField(max_length=200,null=False)
    trainer = models.CharField(max_length=200,null=False)
    start_position = models.IntegerField(default=0)

class Bet(models.Model):
    class Meta:
        unique_together = (('person', 'horse','bet_type'),)
        
    WIN = 'WIN'
    PLACE = 'PLACE'
    SHOW = 'SHOW'
    BET_TYPE_CHOICES = (
        (WIN, 'Win'),
        (PLACE, 'Place'),
        (SHOW, 'Show'),
    )
    person = models.ForeignKey(People, on_delete=models.PROTECT)
    horse = models.ForeignKey(Horse, on_delete=models.PROTECT)
    amount = models.FloatField(default=0.00)
    bet_type = models.CharField(choices=BET_TYPE_CHOICES,max_length=4)
