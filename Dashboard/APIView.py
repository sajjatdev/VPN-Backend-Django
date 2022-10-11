from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import ServerJson, Customer
from .API import ServerJsonSerializer, CustomerSerializer
from .filters import CustomerFilter


class UpdateViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = ServerJson.objects.all()
    serializer_class = ServerJsonSerializer


class CustomerViewSet(ModelViewSet):

    permission_classes = (IsAuthenticated,)
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CustomerFilter
