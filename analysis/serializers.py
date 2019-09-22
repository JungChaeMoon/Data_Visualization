from rest_framework import serializers
from .models import DataModel, DataSaveModel


class DataSaveModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataSaveModel
        fields = (
            'data_model',
            'weight',
            'gyrox',
            'gyroy',
            'gyroz',
            'accelx',
            'accely',
            'accelz',
            'timestamp',
        )
