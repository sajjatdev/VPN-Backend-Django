from dataclasses import fields
from rest_framework import serializers
from .models import update,Customer


class UpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = update
        fields = "__all__"


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = "__all__"
