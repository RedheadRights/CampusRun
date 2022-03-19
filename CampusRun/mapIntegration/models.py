from django.db import models

class route(models.Model):
    routeName = models.TextField(default='')
    addr1 = models.TextField()
    addr2 = models.TextField()

class runData(models.Model):
    path = models.ForeignKey('route', on_delete=models.CASCADE)
    distance = models.FloatField(default=0)
    time = models.IntegerField()
    name = models.TextField()