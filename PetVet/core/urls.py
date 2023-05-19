from django.urls import path
from .views import IndexView, MedicalCareList, PetList, TutorList,  VetList, GeneralClinicList, PhysicalExamList, GeneralDhermExamList, PetAllCareList
from .views import MedicalCareDetail, PetDetail, TutorDetail, GeneralClinicDetail, PhysicalExamDetail, GeneralDhermExamDetail
from .views import MedicalCareCreate, PetCreate, TutorCreate, VetCreate, GeneralClinicCreate, PhysicalExamCreate, GeneralDhermExamCreate
from .views import MedicalCareUpdate, PetUpdate, TutorUpdate, VetUpdate, GeneralClinicUpdate, PhysicalExamUpdate, GeneralDhermExamUpdate
from .views import MedicalCareDelete, PetDelete, TutorDelete, VetDelete, GeneralClinicDelete, PhysicalExamDelete, GeneralDhermExamDelete


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

    path('pet_all_care_list/<int:pk>', PetAllCareList.as_view(), name='pet_all_care_list'),

    path('pets/', PetList.as_view(), name='pets'),
    path('pet/<int:pk>', PetDetail.as_view(), name='pet_detail'),
    path('pet_new/', PetCreate.as_view(), name='pet_new'),
    path('pet_edit/<int:pk>', PetUpdate.as_view(), name='pet_edit'),
    path('pet_delete/<int:pk>', PetDelete.as_view(), name='pet_delete'),


    path('tutors/', TutorList.as_view(), name='tutors'),
    path('tutor/<int:pk>', TutorDetail.as_view(), name='tutor_detail'),
    path('tutor_new/', TutorCreate.as_view(), name='tutor_new'),
    path('tutor_edit/<int:pk>', TutorUpdate.as_view(), name='tutor_edit'),
    path('tutor_delete/<int:pk>', TutorDelete.as_view(), name='tutor_delete'),


    path('vets/', VetList.as_view(), name='vets'),
    path('vet_new/', VetCreate.as_view(), name='vet_new'),
    path('vet_edit/<int:pk>', VetUpdate.as_view(), name='vet_edit'),
    path('vet_delete/<int:pk>', VetDelete.as_view(), name='vet_delete'),


    path('general_clinics/', GeneralClinicList.as_view(), name='general_clinics'),
    path('general_clinic/<int:pk>', GeneralClinicDetail.as_view(),
         name='general_clinic_detail'),
    path('general_clinic_new/', GeneralClinicCreate.as_view(),
         name='general_clinic_new'),
    path('general_clinic_edit/<int:pk>',
         GeneralClinicUpdate.as_view(), name='general_clinic_edit'),
    path('general_clinic_delete/<int:pk>',
         GeneralClinicDelete.as_view(), name='general_clinic_delete'),


    path('physical_exams/', PhysicalExamList.as_view(), name='physical_exams'),
    path('physical_exam/<int:pk>', PhysicalExamDetail.as_view(),
         name='physical_exam_detail'),
    path('physical_exam_new/', PhysicalExamCreate.as_view(),
         name='physical_exam_new'),
    path('physical_exam_edit/<int:pk>',
         PhysicalExamUpdate.as_view(), name='physical_exam_edit'),
    path('physical_exam_delete/<int:pk>',
         PhysicalExamDelete.as_view(), name='physical_exam_delete'),


    path('general_dherm_exams/', GeneralDhermExamList.as_view(), name='general_dherm_exams'),
    path('general_dherm_exam/<int:pk>', GeneralDhermExamDetail.as_view(),
         name='general_dherm_exam_detail'),
    path('general_dherm_exam_new/', GeneralDhermExamCreate.as_view(),
         name='general_dherm_exam_new'),
    path('general_dherm_exam_edit/<int:pk>',
         GeneralDhermExamUpdate.as_view(), name='general_dherm_exam_edit'),
    path('general_dherm_exam_delete/<int:pk>',
         GeneralDhermExamDelete.as_view(), name='general_dherm_exam_delete'),
]
