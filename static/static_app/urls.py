from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('home', views.home, name="home"),
    path('login', views.loginUser, name="login"),
    path('register', views.registerUser, name="register"),

]


