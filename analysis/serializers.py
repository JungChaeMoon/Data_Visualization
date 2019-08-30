from rest_framework import serializers
from .models import DataModel1, DataModel2


class DataModel1Serializer(serializers.ModelSerializer):
    class Meta:
        model = DataModel1
        fields = '__all__'


class DataModel2Serializer(serializers.ModelSerializer):
    class Meta:
        model = DataModel2
        fields = '__all__'
