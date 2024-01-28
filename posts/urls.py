from django.contrib import admin
from django.urls import path
from posts import views
from posts.views import (
    CreatePostView,
    ListPostView,
    UpdatePostView,
)

app_name = "posts"
urlpatterns = [
    path("list-posts", ListPostView.as_view(), name="list-posts"),#as_virew() vì trong ListPostView còn hàm logic render ra hmtl
    path("create-post", CreatePostView.as_view(), name="create-post"),
    path("update-post/<int:pk>/", UpdatePostView.as_view(), name="update-post"),
    path("delete-post/<int:pk>/", views.delete_post, name="delete-post"),
]
