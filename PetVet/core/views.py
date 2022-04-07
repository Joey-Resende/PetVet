from core.models import MedicalCare, Pets, Tutor, Vet
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView


# Views Index
class IndexView(TemplateView):
    template_name = 'core/index.html'
    num_pets = Pets.objects.all().count()
    num_tutors = Tutor.objects.all().count()
    num_medical_care = MedicalCare.objects.all().count()


# Views Medical Care
class MedicalCareList(LoginRequiredMixin, ListView):
    login_url = '/accounts/login/'
    model = MedicalCare
    template_name = 'core/medical_care_list.html'


class MedicalCareDetail(LoginRequiredMixin, TemplateView):
    login_url = '/accounts/login/'
    model = MedicalCare
    context_object_name = 'medicalcare_detail'
    template_name = 'core/medicalcare_detail.html'


class MedicalCareCreate(CreateView):
    model = MedicalCare
    fields = ['date', 'time', 'pet_name',
              'procedure', 'vet_name', 'sedative', 'report']
    template_name = 'core/form.html'
    success_url = reverse_lazy('medical_cares')


class MedicalCareUpdate(UpdateView):
    model = MedicalCare
    fields = ['date', 'time', 'pet_name',
              'procedure', 'vet_name', 'sedative', 'report']
    template_name = 'core/form.html'
    success_url = reverse_lazy('medical_cares')


class MedicalCareDelete(DeleteView):
    model = MedicalCare
    template_name = 'core/form_delete.html'
    success_url = reverse_lazy('medical_cares')


# Views Pet
class PetList(LoginRequiredMixin, ListView):
    login_url = '/accounts/login/'
    model = Pets
    template_name = 'core/pet_list.html'


class PetDetail(LoginRequiredMixin, TemplateView):
    login_url = '/accounts/login/'
    model = Pets


class PetCreate(CreateView):
    model = Pets
    fields = ['pet_name', 'species', 'breed', 'gender',
              'date_of_birth', 'castrated', 'weight', 'tutor_name']
    template_name = 'core/form.html'
    success_url = reverse_lazy('index')


class PetUpdate(UpdateView):
    model = Pets
    fields = ['pet_name', 'species', 'breed', 'gender',
              'date_of_birth', 'castrated', 'weight', 'tutor_name']
    template_name = 'core/form.html'
    success_url = reverse_lazy('index')


class PetDelete(DeleteView):
    model = Pets
    template_name = 'core/form_delete.html'
    success_url = reverse_lazy('index')


# Views Tutor
class TutorList(LoginRequiredMixin, ListView):
    login_url = '/accounts/login/'
    model = Tutor
    template_name = 'core/tutor_list.html'


class TutorDetail(LoginRequiredMixin, TemplateView):
    login_url = '/accounts/login/'
    model = Tutor


class TutorCreate(CreateView):
    model = Tutor
    fields = ['tutor_name', 'cpf', 'phone', 'email', 'cep',
              'street', 'number', 'district', 'city', 'state']
    template_name = 'core/form.html'
    success_url = reverse_lazy('index')


class TutorUpdate(UpdateView):
    model = Tutor
    fields = ['tutor_name', 'cpf', 'phone', 'email', 'cep',
              'street', 'number', 'district', 'city', 'state']
    template_name = 'core/form.html'
    success_url = reverse_lazy('index')


class TutorDelete(DeleteView):
    model = Tutor
    template_name = 'core/form_delete.html'
    success_url = reverse_lazy('index')


# Views Vet
class VetList(LoginRequiredMixin, ListView):
    login_url = '/accounts/login/'
    model = Vet
    template_name = 'core/vet_list.html'


class VetCreate(CreateView):
    model = Vet
    fields = ['vet_name']
    template_name = 'core/form.html'
    success_url = reverse_lazy('index')


class VetUpdate(UpdateView):
    model = Vet
    fields = ['vet_name']
    template_name = 'core/form.html'
    success_url = reverse_lazy('index')


class VetDelete(DeleteView):
    model = Vet
    template_name = 'core/form_delete.html'
    success_url = reverse_lazy('index')
