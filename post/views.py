from django.shortcuts import render
from rest_framework import status, views
from rest_framework.response import Response
from .models import Post, User, Place, Anime
from accounts.models import User, AccessToken
from .serializers import PostSerializer, CreatePostSerializer
from rest_framework import viewsets
from rest_framework.views import APIView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from rest_framework import generics, permissions
from rest_framework import serializers

# 投稿一覧表示
class ListPostsView(views.APIView):
    def get_queryset(self):
        return Post.objects.all()
    
    def get(self, request, *args, **kwargs):
        posts = self.get_queryset()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    

# 聖地の場所の投稿を表示する処理
class PostAPIView(APIView):
    def get_queryset(self):
        return Post.objects.all()

    def get(self, request, **kwargs):
        try:
            placeid = kwargs['placeid']
            post = self.get_queryset().filter(placeid=placeid)
            serializer = PostSerializer(post,many=True)
            return Response(serializer.data)
        except Post.DoesNotExist:
            return Response(status=404)



# 投稿機能
from rest_framework.authentication import TokenAuthentication

class CreatePostView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]  # アクセストークンを利用するための認証クラスを追加

    def perform_create(self, serializer):
        placeid = self.kwargs.get('placeid')
        animeid = self.request.data.get('animeid')
        place = Place.objects.get(id=placeid)
        anime = Anime.objects.get(id=animeid)

        # アクセストークンの検証
        user = self.request.user
        access_token = AccessToken.objects.filter(user=user).first()

        if access_token:
            # アクセストークンが存在する場合は投稿を作成
            serializer.save(userid=user, placeid=place, animeid=anime)
        else:
            # アクセストークンが存在しない場合はエラーを返す
            raise serializers.ValidationError('アクセストークンが無効です')
