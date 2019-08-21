from django.db import models

# Create your models here.


class Data(models.Model):
    weight = models.IntegerField()
    gyro = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

