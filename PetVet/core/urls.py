from django.urls import path
from .views import IndexView, MedicalCareDetailView, MedicalCareListView, MedicalCareCreate, PetDetailView, PetListView, PetCreate, TutorDetailView, TutorListView, TutorCreate, VetListView, VetCreate

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('medical_cares/', MedicalCareListView.as_view(), name='medical_cares'),
    path('medical_care/<int:pk>', MedicalCareDetailView.as_view(),
         name='medical_care-detail'),
    path('medical_care_new/', MedicalCareCreate.as_view(), name='medical_care_new'),
    path('pets/', PetListView.as_view(), name='pets'),
    path('pet/<int:pk>', PetDetailView.as_view(), name='pet-detail'),
    path('pet_new/', PetCreate.as_view(), name='pet_new'),
    path('tutores/', TutorListView.as_view(), name='tutores'),
    path('tutor/<int:pk>', TutorDetailView.as_view(), name='tutor-detail'),
    path('tutor_new/', TutorCreate.as_view(), name='tutor_new'),
    path('vets/', VetListView.as_view(), name='vets'),
    path('vet_new/', VetCreate.as_view(), name='vet_new'),
]
