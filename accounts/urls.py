from django.urls import path
from . import views


urlpatterns = [

    path('login/',views.LoginPage, name="login_page"),
    path('',views.home, name="home"),
    path('logout/',views.logout, name="logout"),





]