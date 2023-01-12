from rest_framework import viewsets, serializers
from rest_framework.views import APIView
from .models import Medidor, Medicion

class MedidorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medidor
        fields = ('llave', 'nombre')

class MedidorViewSet(viewsets.ModelViewSet):
    queryset = Medidor.objects.all()
    serializer_class = MedidorSerializer

class MedicionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicion
        fields = ('medidor', 'fecha_hora', 'consumo')

class MedicionViewSet(viewsets.ModelViewSet):
    queryset = Medicion.objects.all()
    serializer_class = MedicionSerializer


class MedicionMaximaView(APIView):
    def get(self, request, medidor_id):
        medicion_maxima = Medicion.objects.filter(medidor=medidor_id).order_by('-consumo').first()
        serializer = MedicionSerializer(medicion_maxima)
        return Response(serializer.data)
