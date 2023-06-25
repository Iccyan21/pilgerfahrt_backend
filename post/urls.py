from django.urls import path
from .views import CreatePostView, ListPostsView,PostAPIView

urlpatterns = [
    path('', ListPostsView.as_view(), name='list_posts'),
    path('create/', CreatePostView.as_view(), name='create_post'),
    path('posts/<int:placeid>/', PostAPIView.as_view(), name='post-api'),
]
