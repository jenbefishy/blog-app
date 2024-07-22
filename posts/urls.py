from django.urls import path
from .views import PostListView, UserPostListView, create_post, edit_post, delete_post, post_detail

name = "posts"
urlpatterns = [
    path('', PostListView.as_view(), name='index'),
    path('user/<str:username>/', UserPostListView.as_view(), name='user_posts'),
    path('post/<slug:slug>/', post_detail, name='post_detail'),
    path('post/<slug:slug>/edit', edit_post, name='post_edit'),
    path('post/<slug:slug>/delete', delete_post, name='post_delete'),
    path('create/', create_post, name='post_create'),
]
