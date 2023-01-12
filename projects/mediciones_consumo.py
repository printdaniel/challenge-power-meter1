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


class MedicionMinimaView(APIView):
    def get(self, request, llave):
        try:
            medidor = Medidor.objects.get(llave=llave)
            medicion_minima = Medicion.objects.filter(medidor=medidor).order_by('consumo').first()
            serializer = MedicionSerializer(medicion_minima)
            return Response(serializer.data)
        except Medidor.DoesNotExist:
            return Response({"error":"Medidor con llave {} no existe".format(llave)}, status=status.HTTP_404_NOT_FOUND)
