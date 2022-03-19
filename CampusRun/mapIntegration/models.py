from django.db import models

class route(models.Model):
    routeName = models.TextField(default='')
    addr1Lat = models.FloatField(default=0)
    addr1Lng = models.FloatField(default=0)
    addr2Lat = models.FloatField(default=0)
    addr2Lng = models.FloatField(default=0)

class runData(models.Model):
    path = models.ForeignKey('route', on_delete=models.CASCADE)
    distance = models.FloatField(default=0)
    time = models.IntegerField()
    name = models.TextField()