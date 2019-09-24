from django.views.generic import TemplateView

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import DataSaveModel
from .serializers import DataSaveModelSerializer

from math import sqrt


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

        gyrox = sum(list(gyro1x)[0] + list(gyro2x)[0] + list(gyro3x)[0])
        gyroy = sum(list(gyro1y)[0] + list(gyro2y)[0] + list(gyro3y)[0])
        gyroz = sum(list(gyro1z)[0] + list(gyro2z)[0] + list(gyro3z)[0])

        accelx = sum(list(accel1x)[0] + list(accel2x)[0] + list(accel3x)[0])
        accely = sum(list(accel1y)[0] + list(accel2y)[0] + list(accel3y)[0])
        accelz = sum(list(accel1z)[0] + list(accel2z)[0] + list(accel3z)[0])

        torque = sqrt(sum(list(accel1z)[0])*sum(list(accel1z)[0]) + sum(list(accel2z)[0])*sum(list(accel2z)[0]) + sum(list(accel3z)[0])*sum(list(accel3z)[0]))

        data = {
            'weight1': weight1,
            'weight2': weight2,
            'weight3': weight3,
            'first_weight1': first_weight1,
            'timestamp1': timestamp1,
            'timestamp2': timestamp2,
            'gyrox': gyrox,
            'gyroy': gyroy,
            'gyroz': gyroz,
            'accelx': accelx,
            'accely': accely,
            'accelz': accelz,
            'torque': torque,
        }

        return Response(data)


class DataCharView(TemplateView):
    template_name = 'analysis/graph.html'
