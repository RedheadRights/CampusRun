from django.db import models

class runData(models.Model):
    addr1 = models.TextField()
    addr2 = models.TextField()
    time = models.IntegerField()

