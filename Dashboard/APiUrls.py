

from rest_framework.routers import DefaultRouter
from .APIView import UpdateViewSet
route = DefaultRouter()
route.register('update', UpdateViewSet, basename='updateapi')

urlpatterns = route.urls
