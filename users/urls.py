from django.urls import path
from django.conf.urls import include, url

from . import views

app_name = 'users'
urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('', include("django.contrib.auth.urls")),
]