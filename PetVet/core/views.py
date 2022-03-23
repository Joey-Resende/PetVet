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


class PetsListView(generic.ListView):
    model = Pets


#######
