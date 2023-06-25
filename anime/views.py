from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from rest_framework import viewsets
from .models import Anime
from .serializers import AnimeSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
# Create your views here.

# 全て表示する処理
class AnimeListAPIView(APIView):
    def get(self, request):
        anime = Anime.objects.all()
        serializer = AnimeSerializer(anime, many=True)
        return Response(serializer.data)
    
# titleからdataを取得して、APIに送る
class AnimeDetailView(APIView):
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

    def get_queryset(self):
        return Anime.objects.all()

    def get(self, request, title):
        anime = get_object_or_404(Anime, title=title)
        serializer = AnimeSerializer(anime)
        return Response(serializer.data)