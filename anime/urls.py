from django.urls import include, path
from rest_framework import routers
from . import views

urlpatterns = [
    path('', views.AnimeListAPIView.as_view()),
    path('<str:title>/', views.AnimeDetailView.as_view()),    
]