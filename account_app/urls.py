from django.urls import path
from account_app import views

app_name = "account_app"

urlpatterns = [
    path("login/", views.login_page, name="login_page"),
    path("logout/", views.logout_page, name="logout_page"),
    path("register/", views.registration_page, name="registration_page"),
]