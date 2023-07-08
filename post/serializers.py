from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['postid','userid','placeid','animeid','title','description', 'postimage','created_at']
        


class CreatePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['userid', 'placeid', 'placename', 'animeid', 'title', 'description', 'postimage']

