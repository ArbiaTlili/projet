from django.urls import path
from . import views


urlpatterns = [

    path('login/',views.LoginPage, name="login_page"),
    path('',views.HomePage, name="home_page"),





]