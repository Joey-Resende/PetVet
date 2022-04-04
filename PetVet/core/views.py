from core.models import MedicalCare, Pets, Tutor, Vet
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'core/base_model.html'
    num_pets = Pets.objects.all().count()
    num_tutors = Tutor.objects.all().count()
    num_medical_care = MedicalCare.objects.all().count()
    #num_visits = request.session.get('num_visits', 0)
    #request.session['num_visits'] = num_visits + 1


'''
class MedicalCareListView(LoginRequiredMixin, generic.ListView):
    login_url = '/accounts/login/'
    model = MedicalCare
    context_object_name = 'medical_care_list'
    template_name = 'core/medical_care_list.html'
    paginate_by = 10


class MedicalCareDetailView(LoginRequiredMixin, generic.DetailView):
    login_url = '/accounts/login/'
    model = MedicalCare


class PetListView(LoginRequiredMixin, generic.ListView):
    login_url = '/accounts/login/'
    model = Pets
    context_object_name = 'pet_list'
    template_name = 'core/pet_list.html'
    paginate_by = 10


class PetDetailView(LoginRequiredMixin, generic.DetailView):
    login_url = '/accounts/login/'
    model = Pets


class TutorListView(LoginRequiredMixin, generic.ListView):
    login_url = '/accounts/login/'
    model = Tutor
    context_object_name = 'tutor_list'
    template_name = 'core/tutor_list.html'
    paginate_by = 10


class TutorDetailView(LoginRequiredMixin, generic.DetailView):
    login_url = '/accounts/login/'
    model = Tutor

'''


class VetListView(LoginRequiredMixin, TemplateView):
    login_url = '/accounts/login/'
    model = Vet
    context_object_name = 'vet_list'
    template_name = 'core/vet_list.html'
    paginate_by = 10
