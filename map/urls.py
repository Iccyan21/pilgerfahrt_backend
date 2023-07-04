from django.urls import path
from .views import PlaceDataAPI,PlaceDataIntAPI,PlaceSearchAPIView,DirectionsView

urlpatterns = [
    path('<str:name>/', PlaceDataAPI.as_view(), ), #nameで聖地の場所を取得
    path('anime/<int:animeid>/', PlaceDataIntAPI.as_view(), name='place-int-api'), #animeidで聖地の紐づいている場所
    path('places/search/', PlaceSearchAPIView.as_view(), name='place-search'), #聖地を検索する
    path('guide/directions/', DirectionsView.as_view(), name='place-guide'), #場所まで案内する
]
