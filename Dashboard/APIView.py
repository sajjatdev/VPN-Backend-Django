from rest_framework.viewsets import ModelViewSet
from .models import update
from .API import UpdateSerializer


class UpdateViewSet(ModelViewSet):
    queryset = update.objects.all()
    serializer_class = UpdateSerializer
