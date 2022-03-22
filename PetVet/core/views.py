from core.models import SpeciesOfPet, Procedures, Doctor
from django.shortcuts import render


def index(request):
    """View function for home page site."""
    num_procedures = Procedures.objects.all().count()

    context = {
        'num_procedures': num_procedures,
    }

    return render(request, 'index.html', context=context)


# Create your views here.
