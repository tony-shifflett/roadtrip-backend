from django.shortcuts import render
from api.models import Roadtrip
from api.serializers import RoadtripSerializer
from rest_framework.viewsets import ModelViewSet

# Create your views here.
class RoadtripViews(ModelViewSet):
    queryset = Roadtrip.objects.all()
    serializer_class = RoadtripSerializer