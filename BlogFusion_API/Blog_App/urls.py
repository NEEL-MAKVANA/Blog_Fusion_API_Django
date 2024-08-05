from django.urls import path
from .views import (
    author_list,
    author_detail,
    category_list,
    category_detail,
    tag_list,
    tag_detail,
    post_list,
    post_detail,
    comment_list,
    comment_detail,
)

urlpatterns = [
    path("authors/", author_list, name="author_list"),
    path("authors/<uuid:pk>/", author_detail, name="author_detail"),
    path("categories/", category_list, name="category_list"),
    path("categories/<uuid:pk>/", category_detail, name="category_detail"),
    path("tags/", tag_list, name="tag_list"),
    path("tags/<uuid:pk>/", tag_detail, name="tag_detail"),
    path("posts/", post_list, name="post_list"),
    path("posts/<uuid:pk>/", post_detail, name="post_detail"),
    path("comments/", comment_list, name="comment_list"),
    path("comments/<uuid:pk>/", comment_detail, name="comment_detail"),
]
