from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Medicion, Medidor
from .views import MedicionSerializer

class MedicionMaximaView(APIView):
    def get(self, request, llave):
        medidor = Medidor.objects.get(llave=llave)
        medicion_maxima = Medicion.objects.filter(medidor=medidor).order_by('-consumo').first()
        serializer = MedicionSerializer(medicion_maxima)
        return Response(serializer.data)
