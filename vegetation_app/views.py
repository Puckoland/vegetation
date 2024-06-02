from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from .models import Plant
from .serializers import PlantSerializer

from .azure_bus import send_plant


class PlantList(ListCreateAPIView):
    serializer_class = PlantSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        send_plant(serializer.data)

    def get_queryset(self):
        return Plant.objects.filter(owner=self.request.user)


class PlantDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = PlantSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Plant.objects.filter(owner=self.request.user)
