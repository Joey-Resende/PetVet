from core.models import Pets
from django.shortcuts import render
from django.views import generic


def index(request):
    """View function for home page site."""
    num_pets = Pets.objects.all().count()

    context = {
        'num_pets': num_pets,
    }

    return render(request, 'index.html', context=context)


class PetsListView(generic.ListView):
    model = Pets
