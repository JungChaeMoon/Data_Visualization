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
        weight1 = DataSaveModel.objects.filter(data_model=1).values_list('weight').order_by('-timestamp')[:1]
        weight2 = DataSaveModel.objects.filter(data_model=2).values_list('weight').order_by('-timestamp')[:1]
        weight3 = DataSaveModel.objects.filter(data_model=3).values_list('weight').order_by('-timestamp')[:1]
        first_weight1 = DataSaveModel.objects.filter(data_model=1).values_list('weight').order_by('-timestamp')[:50]
        first_weight2 = DataSaveModel.objects.filter(data_model=2).values_list('weight')
        first_weight3 = DataSaveModel.objects.filter(data_model=3).values_list('weight')
        timestamp1 = DataSaveModel.objects.filter(data_model=1).values_list('timestamp').order_by()[:30]
        timestamp2 = DataSaveModel.objects.filter(data_model=2).values_list('timestamp').order_by()[:30]
        timestamp3 = DataSaveModel.objects.filter(data_model=3).values_list('timestamp').order_by()[:30]
        gyro1x = DataSaveModel.objects.filter(data_model=1).values_list('gyrox').order_by('-timestamp')[:1]
        gyro1y = DataSaveModel.objects.filter(data_model=1).values_list('gyroy').order_by('-timestamp')[:1]
        gyro1z = DataSaveModel.objects.filter(data_model=1).values_list('gyroz').order_by('-timestamp')[:1]
        gyro2x = DataSaveModel.objects.filter(data_model=2).values_list('gyrox').order_by('-timestamp')[:1]
        gyro2y = DataSaveModel.objects.filter(data_model=2).values_list('gyroy').order_by('-timestamp')[:1]
        gyro2z = DataSaveModel.objects.filter(data_model=2).values_list('gyroz').order_by('-timestamp')[:1]
        gyro3x = DataSaveModel.objects.filter(data_model=3).values_list('gyrox').order_by('-timestamp')[:1]
        gyro3y = DataSaveModel.objects.filter(data_model=3).values_list('gyroy').order_by('-timestamp')[:1]
        gyro3z = DataSaveModel.objects.filter(data_model=3).values_list('gyroz').order_by('-timestamp')[:1]
        accel1x = DataSaveModel.objects.filter(data_model=1).values_list('accelx').order_by('-timestamp')[:1]
        accel1y = DataSaveModel.objects.filter(data_model=1).values_list('accely').order_by('-timestamp')[:1]
        accel1z = DataSaveModel.objects.filter(data_model=1).values_list('accelz').order_by('-timestamp')[:1]
        accel2x = DataSaveModel.objects.filter(data_model=2).values_list('accelx').order_by('-timestamp')[:1]
        accel2y = DataSaveModel.objects.filter(data_model=2).values_list('accely').order_by('-timestamp')[:1]
        accel2z = DataSaveModel.objects.filter(data_model=2).values_list('accelz').order_by('-timestamp')[:1]
        accel3x = DataSaveModel.objects.filter(data_model=3).values_list('accelx').order_by('-timestamp')[:1]
        accel3y = DataSaveModel.objects.filter(data_model=3).values_list('accely').order_by('-timestamp')[:1]
        accel3z = DataSaveModel.objects.filter(data_model=3).values_list('accelz').order_by('-timestamp')[:1]

        data = {
            'weight1': weight1,
            'weight2': weight2,
            'weight3': weight3,
            'first_weight1': first_weight1,
            'timestamp1': timestamp1,
            'timestamp2': timestamp2,
            'gyro1x': gyro1x,
            'gyro2x': gyro2x,
            'gyro3x': gyro3x,
            'gyro1y': gyro1y,
            'gyro2y': gyro2y,
            'gyro3y': gyro3y,
            'gyro1z': gyro1z,
            'gyro2z': gyro2z,
            'gyro3z': gyro3z,
            'accel1x': accel1x,
            'accel2x': accel2x,
            'accel3x': accel3x,
            'accel1y': accel1y,
            'accel2y': accel2y,
            'accel3y': accel3y,
            'accel1z': accel1z,
            'accel2z': accel2z,
            'accel3z': accel3z,
        }


        return Response(data)


class DataCharView(TemplateView):
    template_name = 'analysis/graph.html'
