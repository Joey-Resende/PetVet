from core import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('procedures/', views.ProceduresListView.as_view(), name='Procedures'),
]
