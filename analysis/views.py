from rest_framework import viewsets
from .serializers import DataSerializer
from .models import Data


class DataAnalysisView(viewsets.ModelViewSet):
    queryset = Data.objects.all()
    serializer_class = DataSerializer

    def post(self, request):
        self.serializer_class(data=request.data)

