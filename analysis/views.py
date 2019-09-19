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
        weight = DataSaveModel.objects.values_list('weight').order_by()[:30]
        timestamp = DataSaveModel.objects.values_list('timestamp').order_by()[:30]
        data = {
            'weight': weight,
            'timestamp': timestamp,
        }
        return Response(data)


class DataCharView(TemplateView):
    template_name = 'analysis/graph.html'
