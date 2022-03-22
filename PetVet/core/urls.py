from core import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('pets/', views.PetsListView.as_view(), name='Pets'),
]
