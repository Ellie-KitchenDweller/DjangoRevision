from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.RecentPostsView.as_view(), name='forum'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),
]