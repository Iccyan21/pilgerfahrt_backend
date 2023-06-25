from rest_framework import serializers
from .models import Place

#このdataをAPIのdataに送る
class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ['placeid','animeid','name', 'address','descpiption','notes','accsess','placeimage','lat','lng']  # シリアライズするフィールドのリスト
        