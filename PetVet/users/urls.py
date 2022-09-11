from django.urls import path
from django.contrib.auth import views as auth_views
from .views import UserCreate, ProfileUpdate

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(
        template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', UserCreate.as_view(), name='registrar'),
    path('update_profile/', ProfileUpdate.as_view(), name='meus_dados'),
]
