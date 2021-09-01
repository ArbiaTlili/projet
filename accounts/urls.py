from django.urls import path
from . import views


urlpatterns = [

    path('login/',views.LoginPage, name="login_page"),
    path('/home/',views.home1, name="home1"),
    path('logout/',views.logout, name="logout"),





]