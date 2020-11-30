from django.urls import include, path
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

from users import views

router = DefaultRouter()
router.register(r'hackathons', views.HackathonViewset, basename='hackathon')

urlpatterns = [
    path('profiles/<str:username>/', views.ProfileDetail.as_view()),
    path('profiles/add_language/<str:username>/', views.add_language),
    path('', include(router.urls)),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
