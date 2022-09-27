from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import update, Customer
from .API import UpdateSerializer, CustomerSerializer
from .filters import CustomerFilter


class UpdateViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = update.objects.all()
    serializer_class = UpdateSerializer


class CustomerViewSet(ModelViewSet):

    permission_classes = (IsAuthenticated,)
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CustomerFilter
