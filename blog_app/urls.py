from django.urls import path
from blog_app import views

app_name = "blog_app"
urlpatterns = [
    path("", views.post_list, name="post_list"),
]