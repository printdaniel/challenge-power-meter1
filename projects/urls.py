from django.urls import path, include
from rest_framework import routers
from .views import MedidorViewSet, MedicionViewSet

router = routers.DefaultRouter()
router.register('medidores', MedidorViewSet)
router.register('mediciones', MedicionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
