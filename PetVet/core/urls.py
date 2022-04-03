from .views import IndexView
from django.urls import path

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    #path('medical_cares/', views.MedicalCareListView.as_view(), name='medical_cares'),
    # path('medical_care/<int:pk>',
    #     views.MedicalCareDetailView.as_view(), name='medical_care-detail'),
    #path('pets/', views.PetListView.as_view(), name='pets'),
    #path('pet/<int:pk>', views.PetDetailView.as_view(), name='pet-detail'),
    #path('tutores/', views.TutorListView.as_view(), name='tutores'),
    #path('tutor/<int:pk>', views.TutorDetailView.as_view(), name='tutor-detail'),
    #path('vets/', views.VetListView.as_view(), name='vets'),
]
