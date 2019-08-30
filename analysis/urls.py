from django.urls import path, include
from rest_framework import routers
from .views import DataModel1SaveView, DataModel2SaveView, GraphView

app_name = 'analysis'

router = routers.DefaultRouter()
router.register('data1_save', DataModel1SaveView)
router.register('data2_save', DataModel2SaveView)

urlpatterns = [
    path('', include(router.urls)),
    path('graph/', GraphView.as_view(), name='graph'),
]
