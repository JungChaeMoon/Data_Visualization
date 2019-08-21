from django.urls import path, include
from rest_framework import routers
from .views import DataAnalysisView

app_name = 'analysis'

router = routers.DefaultRouter()
router.register('data', DataAnalysisView)

urlpatterns = [
    path('', include(router.urls))
]
