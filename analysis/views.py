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
        # first_weight1 = DataSaveModel.objects.filter(data_model=1).values_list('weight').order_by('-timestamp')[:50]
        # first_weight2 = DataSaveModel.objects.filter(data_model=2).values_list('weight')
        # first_weight3 = DataSaveModel.objects.filter(data_model=3).values_list('weight')
        # timestamp1 = DataSaveModel.objects.filter(data_model=1).values_list('timestamp').order_by()[:30]
        # timestamp2 = DataSaveModel.objects.filter(data_model=2).values_list('timestamp').order_by()[:30]
        # timestamp3 = DataSaveModel.objects.filter(data_model=3).values_list('timestamp').order_by()[:30]
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

        gyrox = sum(i[0] for i in list(gyro1x)) + sum(i[0] for i in list(gyro2x)) + sum(i[0] for i in list(gyro3x))
        gyroy = sum(i[0] for i in list(gyro1y)) + sum(i[0] for i in list(gyro2y)) + sum(i[0] for i in list(gyro3y))
        gyroz = sum(i[0] for i in list(gyro1z)) + sum(i[0] for i in list(gyro2z)) + sum(i[0] for i in list(gyro3z))

        accelx = sum(i[0] for i in list(accel1x)) + sum(i[0] for i in list(accel2x)) + sum(i[0] for i in list(accel3x))
        accely = sum(i[0] for i in list(accel1y)) + sum(i[0] for i in list(accel2y)) + sum(i[0] for i in list(accel3y))
        accelz = sum(i[0] for i in list(accel1z)) + sum(i[0] for i in list(accel2z)) + sum(i[0] for i in list(accel3z))

        # torque = sqrt(sum(i[0] for i in list(accel1z))*sum(i[0] for i in list(accel1z)) + sum(i[0] for i in list(accel2z))*sum(i[0] for i in list(accel2z)) + sum(i[0] for i in list(accel3z))*sum(i[0] for i in list(accel3z)))

        data = {
            'weight1': weight1,
            'weight2': weight2,
            'weight3': weight3,
            'gyrox': gyrox,
            'gyroy': gyroy,
            'gyroz': gyroz,
            'accelx': accelx,
            'accely': accely,
            'accelz': accelz,
            # 'torque': torque,
        }

        return Response(data)


class DataCharView(TemplateView):
    template_name = 'analysis/graph.html'
