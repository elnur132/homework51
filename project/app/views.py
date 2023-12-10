from rest_framework.viewsets import ModelViewSet
from .models import CarBrand, Car
from .serializers import CarBrandSerializer, CarSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView

# Create your views here.
class CarBrandCreateView(CreateAPIView):
    queryset = CarBrand.objects.all()
    serializer_class = CarBrandSerializer


class CarCreateView(CreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    
class CarViewSet(ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer