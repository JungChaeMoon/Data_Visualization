from django.db import models

# Create your models here.


class DataModel1(models.Model):
    weight = models.IntegerField()
    gyro = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)


class DataModel2(models.Model):
    weight = models.IntegerField()
    gyro = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
