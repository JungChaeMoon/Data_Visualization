from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView
from rest_framework import viewsets
from .models import Data
from .serializers import DataSerializer


class DataSaveView(viewsets.ModelViewSet):
    queryset = Data.objects.all()
    serializer_class = DataSerializer

    def create(self, request, *args, **kwargs):
        response = super(DataSaveView, self).create(request, *args, **kwargs)
        return HttpResponseRedirect(reverse('data_list'))


class GraphView(TemplateView):
    template_name = 'analysis/graph.html'

    def get(self, request, *args, **kwargs):
        return super(GraphView, self).get(request, *args, **kwargs)
