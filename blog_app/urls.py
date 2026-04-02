from django.urls import path
from blog_app import views

app_name = "blog_app"
urlpatterns = [
    path("posts", views.post_list, name="post_list"),
    path("post/<slug:slug>", views.post_detail, name="post_detail"),
    path("category/<int:pk>",views.category_detail , name="category_detail")
]