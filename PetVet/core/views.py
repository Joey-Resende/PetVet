from core.models import MedicalCare, Pets, Tutor, Vet
from django.shortcuts import render
from django.views import generic


def index(request):
    """View function for home page site."""
    num_pets = Pets.objects.all().count()
    num_tutors = Tutor.objects.all().count()
    num_medical_care = MedicalCare.objects.all().count()

    context = {
        'num_pets': num_pets,
        'num_tutors': num_tutors,
        'num_medical_care': num_medical_care,
    }

    return render(request, 'index.html', context=context)


class MedicalCareListView(generic.ListView):
    model = MedicalCare
    context_object_name = 'medical_care_list'
    template_name = 'core/medical_care_list.html'
    paginate_by = 10


class MedicalCareDetailView(generic.DetailView):
    model = MedicalCare


class PetListView(generic.ListView):
    model = Pets
    context_object_name = 'pet_list'
    template_name = 'core/pet_list.html'
    paginate_by = 10


class PetDetailView(generic.DetailView):
    model = Pets


class TutorListView(generic.ListView):
    model = Tutor
    context_object_name = 'tutor_list'
    template_name = 'core/tutor_list.html'
    paginate_by = 10


class TutorDetailView(generic.DetailView):
    model = Tutor


class VetListView(generic.ListView):
    model = Vet
    context_object_name = 'vet_list'
    template_name = 'core/vet_list.html'
    paginate_by = 10
