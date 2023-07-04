from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from urllib.parse import unquote
from rest_framework.views import APIView
from .models import Place
from .serializers import PlaceSerializer
from rest_framework.response import Response
from django.db.models import Q
import googlemaps
from django.core.exceptions import ImproperlyConfigured
import os
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
        query = self.request.GET.get('q', '')
        # アニメのtitleに一致する場所を検索する
        return Place.objects.filter(Q(name__icontains=query) | Q(animetitle__title__icontains=query))

    def get(self, request):
        queryset = self.get_queryset()
        serializer = PlaceSerializer(queryset, many=True)

        data = serializer.data

        for item in data:
            item['placeimage'] = unquote(item['placeimage'])

        return Response(data)



class DirectionsView(APIView):
    def get(self, request, *args, **kwargs):
        # 環境変数からAPIキーを取得します
        api_key = os.getenv("GOOGLE_MAPS_API_KEY")
        if not api_key:
            raise ImproperlyConfigured("GOOGLE_MAPS_API_KEY must be set")

        gmaps = googlemaps.Client(key=api_key)

        # クエリパラメータから出発地と目的地を取得します
        start = request.GET.get('start')
        end = request.GET.get('end')
        
        if not start or not end:
            return Response({"error": "start and end parameters are required."}, status=400)

        # APIにリクエストを送信します
        directions_result = gmaps.directions(start, end)

        # レスポンスデータからルート情報だけを抽出します
        if directions_result:
            leg = directions_result[0]['legs'][0]  # Consider only the first route
            steps = []
            for step in leg['steps']:
                steps.append({
                    'start_location': step['start_location'],
                    'end_location': step['end_location'],
                    'html_instructions': step['html_instructions'],
                    'distance': step['distance']['text'],
                    'duration': step['duration']['text'],
                })

            # Return the first route's steps
            return Response(steps)

        # If no routes found
        return Response({"error": "No routes found."}, status=404)


