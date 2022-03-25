from core import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('medical_cares/', views.MedicalCareListView.as_view(), name='medical_cares'),
    path('medical_care/<int:pk>',
         views.MedicalCareDetailView.as_view(), name='medical_care-detail'),
]
