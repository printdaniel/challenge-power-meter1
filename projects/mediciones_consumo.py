from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Medicion, Medidor
from .views import MedicionSerializer
from django.db.models import Sum, Avg

class MedicionMaximaView(APIView):
    def get(self, request, llave):
        try:
            medidor = Medidor.objects.get(llave=llave)
            medicion_maxima = Medicion.objects.filter(medidor=medidor).order_by('-consumo').first()
            serializer = MedicionSerializer(medicion_maxima)
            return Response(serializer.data)
        except Medidor.DoesNotExist:
            return Response({"error":"Medidor con llave {} no existe".format(llave)}, status=status.HTTP_404_NOT_FOUND)


class MedicionMinimaView(APIView):
    def get(self, request, llave):
        try:
            medidor = Medidor.objects.get(llave=llave)
            medicion_minima = Medicion.objects.filter(medidor=medidor).order_by('consumo').first()
            serializer = MedicionSerializer(medicion_minima)
            return Response(serializer.data)
        except Medidor.DoesNotExist:
            return Response({"error":"Medidor con llave {} no existe".format(llave)}, status=status.HTTP_404_NOT_FOUND)


class ConsumoTotalView(APIView):
    def get(self, request, llave):
        try:
            medidor = Medidor.objects.get(llave=llave)
            consumo_total = Medicion.objects.filter(medidor=medidor).aggregate(Sum('consumo'))
            return Response(consumo_total)
        except Medidor.DoesNotExist:
            return Response({"error":"Medidor con llave {} no existe".format(llave)}, status=status.HTTP_404_NOT_FOUND)


class ConsumoPromedioView(APIView):
    def get(self, request, llave):
        try:
            medidor = Medidor.objects.get(llave=llave)
            consumo_promedio = Medicion.objects.filter(medidor=medidor).aggregate(Avg('consumo'))
            return Response(consumo_promedio)
        except Medidor.DoesNotExist:
            return Response({"error":"Medidor con llave {} no existe".format(llave)}, status=status.HTTP_404_NOT_FOUND)
