from rest_framework import generics, status
from rest_framework.response import Response

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


class GraphView(generics.ListAPIView):
    queryset = DataSaveModel.objects.all()
    serializer_class = DataSaveModelSerializer
