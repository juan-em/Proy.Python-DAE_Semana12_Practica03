from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Oferta
from .serializers import OfertaSerializer

class OfertasView(APIView):

    def get(self, request):
        dataSeries = Oferta.objects.all()
        ofertas = OfertaSerializer(dataSeries, many=True)
        return Response(ofertas.data)

    def post(self, request):
        oferta = OfertaSerializer(data=request.data)
        oferta.is_valid(raise_exception=True)
        oferta.save()

        return Response(oferta.data)


class OfertasDetailView(APIView):

    def get(self, request, oferta_id):
        dataoferta = Oferta.objects.get(pk=oferta_id)
        oferta = OfertaSerializer(dataoferta)
        return Response(oferta.data)

    def put(self, request, oferta_id):
        dataoferta = Oferta.objects.get(pk=oferta_id)
        oferta = OfertaSerializer(dataoferta, data=request.data)
        oferta.is_valid(raise_exception=True)
        oferta.save()
        return Response(oferta.data)

    def delete(self, request, oferta_id):
        dataoferta = Oferta.objects.get(pk=oferta_id)
        seroferta = OfertaSerializer(dataoferta)
        dataoferta.delete()
        return Response(seroferta.data)