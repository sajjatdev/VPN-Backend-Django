
from rest_framework.routers import DefaultRouter
from .APIView import UpdateViewSet, CustomerViewSet
route = DefaultRouter()
route.register('update', UpdateViewSet, basename='updateapi')
route.register('customer', CustomerViewSet, basename='customer')
urlpatterns = route.urls
