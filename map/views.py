from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from urllib.parse import unquote
from rest_framework.views import APIView
from .models import Place
from .serializers import PlaceSerializer
from rest_framework.response import Response
# Create your views here.

# getでnameからdataを取得して、APIに送る
class PlaceDataAPI(APIView):
    def get_queryset(self):
        return Place.objects.all()

    def get(self, request, name):
        try:
            customer = self.get_queryset().get(name=name)
            serializer = PlaceSerializer(customer)
            data = serializer.data
            data['placeimage'] = unquote(data['placeimage'])
            return Response(data)
            
        except Place.DoesNotExist:
            return Response(status=404)
        
# getでintからdataを取得して、APIに送る(アニメの詳細画面から聖地の場所に飛ぶのに使用)
class PlaceDataIntAPI(APIView):
    def get_queryset(self):
        return Place.objects.all()

    def get(self, request, animeid):
        try:
            customer = self.get_queryset().filter(animeid=animeid)
            serializer =PlaceSerializer(customer, many=True)
            return Response(serializer.data)
        except Place.DoesNotExist:
            return Response(status=404)

# 場所をSerachする処理    
class PlaceSearchAPIView(APIView):    
    def get_queryset(self):
        # get_querysetメソッドを呼び出して検索結果のクエリセットを取得
        query = self.request.GET.get('q', '')
        return Place.objects.search_by_name(query)

    def get(self, request):
        queryset = self.get_queryset()
        serializer = PlaceSerializer(queryset, many=True)
        return Response(serializer.data)
