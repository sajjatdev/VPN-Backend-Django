from dataclasses import fields
from rest_framework import serializers
from .models import update


class UpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = update
        fields = "__all__"
