from django.urls import path
from users import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('profiles/<str:username>/', views.ProfileDetail.as_view()),
    path('profiles/add_language/<str:username>/', views.add_language),
    path('hackathon/', views.HackathonList.as_view()),
    path('hackathon/<int:pk>/', views.HackathonDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
