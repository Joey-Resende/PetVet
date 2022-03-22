from core.models import SpeciesOfPet, Procedures, Doctor
from django.shortcuts import render
from django.views import generic


def index(request):
    """View function for home page site."""
    num_procedures = Procedures.objects.all().count()

    context = {
        'num_procedures': num_procedures,
    }

    return render(request, 'index.html', context=context)


class ProceduresListView(generic.ListView):
    model = Procedures
