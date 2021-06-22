from django.db.models.base import ModelState
from api.models import Roadtrip
from rest_framework.serializers import ModelSerializer

class RoadtripSerializer (ModelSerializer):
    class Meta:
        model = Roadtrip
        fields = ["id", "name", "numberOfPassengers"]