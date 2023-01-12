from django.urls import path, include
from rest_framework import routers
from .views import MedidorViewSet, MedicionViewSet
from .mediciones_consumo import MedicionMaximaView, MedicionMinimaView, ConsumoTotalView

router = routers.DefaultRouter()
router.register('medidores', MedidorViewSet)
router.register('mediciones', MedicionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('mediciones-maximas/<str:llave>/', MedicionMaximaView.as_view()),
    path('mediciones-minimas/<str:llave>/', MedicionMinimaView.as_view()),
    path('consumo-total/<str:llave>/', ConsumoTotalView.as_view()),
]
