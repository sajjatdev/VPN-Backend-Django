from rest_framework import serializers
from .models import Customer, Payload, Server, ServerJson


class PayloadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payload
        fields = "__all__"


class ServerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Server
        fields = "__all__"


class ServerJsonSerializer(serializers.ModelSerializer):
    payload = PayloadSerializer(many=True)
    server = ServerSerializer(many=True)

    class Meta:
        model = ServerJson
        fields = "__all__"


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = "__all__"
