from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from .forms import Userform
from django.urls import reverse_lazy


class UserCreate(CreateView):
    template_name = 'core/form.html'
    form_class = Userform
    success_url = reverse_lazy('index')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['title_window'] = 'PetVet - Registrar Usúario'
        context['title_page'] = 'Registrar Usúario'
        context['tips'] = 'Preencha os campos para registrar um novo usúario.'

        return context
