from django.urls import path
from django.conf.urls import include, url

from . import views

app_name = 'users'
urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>', views.UserDetail.as_view()),
    path('profile/', views.ProfileView.as_view()),
]