from core import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('medical_care/', views.MedicalCareListView.as_view(), name='medical_care'),
    path('medical_care/<int:pk>',
         views.MedicalCareDetailView.as_view(), name='medical_care-detail'),
]
