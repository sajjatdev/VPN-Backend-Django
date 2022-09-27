from django_filters.rest_framework import FilterSet
from .models import Customer


class CustomerFilter(FilterSet):
    class Meta:

        model = Customer
        fields = {
            'username': ['exact'],
            'password': ['exact'],
            'is_active': ['exact']
        }
