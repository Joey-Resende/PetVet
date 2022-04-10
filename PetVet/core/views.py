from .models import MedicalCare, Pets, Tutor, Vet
from braces.views import GroupRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView, TemplateView


# Views Index
class IndexView(TemplateView):
    template_name = 'core/index.html'
    num_pets = Pets.objects.all().count()
    num_tutors = Tutor.objects.all().count()
    num_medical_care = MedicalCare.objects.all().count()


# Views Medical Care
class MedicalCareList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = MedicalCare
    template_name = 'core/medical_care_list.html'


class MedicalCareDetail(LoginRequiredMixin, DetailView):
    login_url = reverse_lazy('login')
    model = MedicalCare
    template_name = 'core/medicalcare_detail.html'
    success_url = reverse_lazy('medical_cares')


class MedicalCareCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = MedicalCare
    fields = ['date', 'time', 'pet_name',
              'procedure', 'vet_name', 'sedative', 'report']
    template_name = 'core/form.html'
    success_url = reverse_lazy('medical_cares')


class MedicalCareUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = MedicalCare
    fields = ['date', 'time', 'pet_name',
              'procedure', 'vet_name', 'sedative', 'report']
    template_name = 'core/form.html'
    success_url = reverse_lazy('medical_cares')


class MedicalCareDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = [u"Recepcionista", u"Admin"]
    model = MedicalCare
    template_name = 'core/form_delete.html'
    success_url = reverse_lazy('medical_cares')


# Views Pet
class PetList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Pets
    template_name = 'core/pet_list.html'


class PetDetail(LoginRequiredMixin, DetailView):
    login_url = reverse_lazy('login')
    model = Pets
    template_name = 'core/pet_detail.html'
    success_url = reverse_lazy('pets')


class PetCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Pets
    fields = ['pet_name', 'species', 'breed', 'gender',
              'date_of_birth', 'castrated', 'weight', 'tutor_name']
    template_name = 'core/form.html'
    success_url = reverse_lazy('pets')


class PetUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Pets
    fields = ['pet_name', 'species', 'breed', 'gender',
              'date_of_birth', 'castrated', 'weight', 'tutor_name']
    template_name = 'core/form.html'
    success_url = reverse_lazy('pets')


class PetDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = [u"Recepcionista", u"Admin"]
    model = Pets
    template_name = 'core/form_delete.html'
    success_url = reverse_lazy('pets')


# Views Tutor
class TutorList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Tutor
    template_name = 'core/tutor_list.html'


class TutorDetail(LoginRequiredMixin, DetailView):
    login_url = reverse_lazy('login')
    model = Tutor
    template_name = 'core/tutor_detail.html'
    success_url = reverse_lazy('tutors')


class TutorCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Tutor
    fields = ['tutor_name', 'cpf', 'phone', 'email', 'cep',
              'street', 'number', 'district', 'city', 'state']
    template_name = 'core/form.html'
    success_url = reverse_lazy('tutors')


class TutorUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Tutor
    fields = ['tutor_name', 'cpf', 'phone', 'email', 'cep',
              'street', 'number', 'district', 'city', 'state']
    template_name = 'core/form.html'
    success_url = reverse_lazy('tutors')


class TutorDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = [u"Recepcionista", u"Admin"]
    model = Tutor
    template_name = 'core/form_delete.html'
    success_url = reverse_lazy('tutors')


# Views Vet
class VetList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Vet
    template_name = 'core/vet_list.html'


class VetCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Vet
    fields = ['vet_name']
    template_name = 'core/form.html'
    success_url = reverse_lazy('vets')


class VetUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Vet
    fields = ['vet_name']
    template_name = 'core/form.html'
    success_url = reverse_lazy('vets')


class VetDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = [u"Recepcionista", u"Admin"]
    model = Vet
    template_name = 'core/form_delete.html'
    success_url = reverse_lazy('vets')
