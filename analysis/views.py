from django.views.generic import TemplateView

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import DataSaveModel
from .serializers import DataSaveModelSerializer


class DataModelSaveView(generics.CreateAPIView):
    queryset = DataSaveModel.objects.all()
    serializer_class = DataSaveModelSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class GraphView(APIView):

    def get(self, request, *args, **kwargs):
        weight1 = DataSaveModel.objects.filter(data_model=1).values_list('weight').order_by()[:1]
        first_weight = DataSaveModel.objects.filter(data_model=1).values_list('weight')
        timestamp1 = DataSaveModel.objects.filter(data_model=1).values_list('timestamp').order_by()[:30]
        weight2 = DataSaveModel.objects.filter(data_model=2).values_list('weight').order_by()[:30]
        timestamp2 = DataSaveModel.objects.filter(data_model=2).values_list('timestamp').order_by()[:30]

        data = {
            'weight1': weight1,
            'first_weight': first_weight,
            'timestamp1': timestamp1,
            'weight2': weight2,
            'timestamp2': timestamp2,
        }

        # def building_gyro(gyro1x, gyro1y, gyro1z, gyro2x, gyro2y, gyro2z, gyro3x):

        return Response(data)


class DataCharView(TemplateView):
    template_name = 'analysis/graph.html'
