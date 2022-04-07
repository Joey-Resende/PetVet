from core.models import MedicalCare, Pets, Tutor, Vet
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView


class IndexView(TemplateView):
    template_name = 'core/index.html'
    num_pets = Pets.objects.all().count()
    num_tutors = Tutor.objects.all().count()
    num_medical_care = MedicalCare.objects.all().count()


class MedicalCareListView(LoginRequiredMixin, TemplateView):
    login_url = '/accounts/login/'
    model = MedicalCare
    context_object_name = 'medical_care_list'
    template_name = 'core/medical_care_list.html'
    paginate_by = 10


class MedicalCareDetailView(LoginRequiredMixin, TemplateView):
    login_url = '/accounts/login/'
    model = MedicalCare
    context_object_name = 'medicalcare_detail'
    template_name = 'core/medicalcare_detail.html'


class MedicalCareCreate(CreateView):
    model = MedicalCare
    fields = ['date', 'time', 'pet_name',
              'procedure', 'vet_name', 'sedative', 'report']
    template_name = 'core/form.html'
    success_url = reverse_lazy('index')


'''
class PetListView(LoginRequiredMixin, generic.ListView):
    login_url = '/accounts/login/'
    model = Pets
    context_object_name = 'pet_list'
    template_name = 'core/pet_list.html'
    paginate_by = 10


class PetDetailView(LoginRequiredMixin, generic.DetailView):
    login_url = '/accounts/login/'
    model = Pets


class PetCreate(CreateView):
    model = Pet
    fields = ['pet_name', 'species', 'breed', 'gender', 'date_of_birth', 'castrated','weight', 'tutor_name']
    template_name = 'core/form.html'
    success_url = reverse_lazy('index')


class TutorListView(LoginRequiredMixin, generic.ListView):
    login_url = '/accounts/login/'
    model = Tutor
    context_object_name = 'tutor_list'
    template_name = 'core/tutor_list.html'
    paginate_by = 10


class TutorDetailView(LoginRequiredMixin, generic.DetailView):
    login_url = '/accounts/login/'
    model = Tutor


class VetListView(LoginRequiredMixin, TemplateView):
    login_url = '/accounts/login/'
    model = Vet
    context_object_name = 'vet_list'
    template_name = 'core/vet_list.html'
    paginate_by = 10
'''
