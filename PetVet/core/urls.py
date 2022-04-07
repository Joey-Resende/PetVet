from django.urls import path
from .views import IndexView, MedicalCareList, PetList, TutorList,  VetList
from .views import MedicalCareDetail, PetDetail, TutorDetail
from .views import MedicalCareCreate, PetCreate, TutorCreate, VetCreate
from .views import MedicalCareUpdate, PetUpdate, TutorUpdate, VetUpdate
from .views import MedicalCareDelete, PetDelete, TutorDelete, VetDelete


urlpatterns = [
    path('', IndexView.as_view(), name='index'),

    path('medical_cares/', MedicalCareList.as_view(), name='medical_cares'),
    path('medical_care/<int:pk>', MedicalCareDetail.as_view(),
         name='medical_care_detail'),
    path('medical_care_new/', MedicalCareCreate.as_view(), name='medical_care_new'),
    path('medical_care_edit/<int:pk>',
         MedicalCareUpdate.as_view(), name='medical_care_edit'),
    path('medical_care_delete/<int:pk>',
         MedicalCareDelete.as_view(), name='medical_care_delete'),


    path('pets/', PetList.as_view(), name='pets'),
    path('pet/<int:pk>', PetDetail.as_view(), name='pet-detail'),
    path('pet_new/', PetCreate.as_view(), name='pet_new'),
    path('pet_edit/<int:pk>', PetUpdate.as_view(), name='pet_edit'),
    path('pet_delete/<int:pk>', PetDelete.as_view(), name='pet_delete'),


    path('tutors/', TutorList.as_view(), name='tutors'),
    path('tutor/<int:pk>', TutorDetail.as_view(), name='tutor-detail'),
    path('tutor_new/', TutorCreate.as_view(), name='tutor_new'),
    path('tutor_edit/<int:pk>', TutorUpdate.as_view(), name='tutor_edit'),
    path('tutor_delete/<int:pk>', TutorDelete.as_view(), name='tutor_delete'),


    path('vets/', VetList.as_view(), name='vets'),
    path('vet_new/', VetCreate.as_view(), name='vet_new'),
    path('vet_edit/<int:pk>', VetUpdate.as_view(), name='vet_edit'),
    path('vet_delete/<int:pk>', VetDelete.as_view(), name='vet_delete'),
]
