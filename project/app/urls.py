from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import CarCreateView, CarBrandCreateView, CarViewSet

router = DefaultRouter()
router.register('cars', CarViewSet)

urlpatterns = [
    path('carbrand/create/', CarBrandCreateView.as_view(), name='carbrand-create'),
    path('car/create/', CarCreateView.as_view(), name='car-create'),
    path('', include(router.urls)),
]
