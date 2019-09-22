from django.db import models


class DataModel(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class DataSaveModel(models.Model):
    data_model = models.ForeignKey('analysis.DataModel', on_delete=models.CASCADE, related_name='data_save_model')
    weight = models.IntegerField(default=0)
    gyrox = models.IntegerField(default=0, null=True, blank=True)
    gyroy = models.IntegerField(default=0, null=True, blank=True)
    gyroz = models.IntegerField(default=0, null=True, blank=True)
    accelx = models.IntegerField(default=0, null=True, blank=True)
    accely = models.IntegerField(default=0, null=True, blank=True)
    accelz = models.IntegerField(default=0, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
