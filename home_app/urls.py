from django.urls import path
from home_app import views

app_name = "home_app"
urlpatterns = [
    path("", views.home_page, name="home_page"),
    path("contactus/", views.contact_us_page, name="contact_us_page"),
]