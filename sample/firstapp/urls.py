from django.urls import path
from . import views

urlpatterns=[
    path('', views.welcome, name="welcome"),
    path('index',views.index,name="index"),
    path('about', views.about, name="about"),

]
