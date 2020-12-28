from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Car
from .permissions import CarBlocklistPermission, IsCarLegitorReadOnly
from .serializers import CarSerializer
# Create your views here.
class CarList(ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = (CarBlocklistPermission,)

class CarDetail(RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = (IsCarLegitorReadOnly,)