from django.urls import path, include
from rest_framework import routers
from .views import DataModelSaveView, GraphView

app_name = 'analysis'
#
# router = routers.DefaultRouter()
# router.register('data_save', DataModelSaveView)
# router.register('data_list', GraphView)

urlpatterns = [
    path('data_save', DataModelSaveView.as_view(), name='data_save'),
    path('data_list', GraphView.as_view(), name='data_list'),
]
