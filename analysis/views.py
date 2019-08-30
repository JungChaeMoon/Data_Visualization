from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView
from rest_framework import viewsets
from .models import DataModel1, DataModel2
from .serializers import DataModel1Serializer, DataModel2Serializer
import pandas as pd
import numpy as np


class DataModel1SaveView(viewsets.ModelViewSet):
    queryset = DataModel1.objects.all()
    serializer_class = DataModel1Serializer

    def create(self, request, *args, **kwargs):
        response = super(DataModel1SaveView, self).create(request, *args, **kwargs)
        return HttpResponseRedirect(reverse('#'))


class DataModel2SaveView(viewsets.ModelViewSet):
    queryset = DataModel2.objects.all()
    serializer_class = DataModel2Serializer

    def create(self, request, *args, **kwargs):
        reponse = super(DataModel2SaveView, self).create(request, *args, **kwargs)
        return HttpResponseRedirect(reverse('#'))


class GraphView(TemplateView):
    template_name = 'analysis/graph.html'

    def get(self, request, *args, **kwargs):
        return super(GraphView, self).get(request, *args, **kwargs)
