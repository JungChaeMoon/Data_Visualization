from django.urls import path, include
from rest_framework import routers
from .views import DataSaveView, GraphView

app_name = 'analysis'

router = routers.DefaultRouter()
router.register('data_save', DataSaveView)

urlpatterns = [
    path('', include(router.urls)),
    path('graph/', GraphView.as_view(), name='graph'),

]
