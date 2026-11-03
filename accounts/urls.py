from django.urls import path

from accounts.views import AdminCreateView
from accounts.views import StudentCreateView
from accounts.views import ProfileUpdateView
from accounts.views import ProfileDetailView

from rest_framework.authtoken.views import ObtainAuthToken

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView



urlpatterns=[
    path("admin/register/",AdminCreateView.as_view()),
    path("student/register/",StudentCreateView.as_view()),
    path("profile/complete/",ProfileUpdateView.as_view()),
    path("profile/me/",ProfileDetailView.as_view()),

    path("token/",ObtainAuthToken.as_view()),

    path("jwt/token/",TokenObtainPairView.as_view()),
    path("jwt/token/refresh/",TokenRefreshView.as_view()),


]