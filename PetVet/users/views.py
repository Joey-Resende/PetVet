from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.models import User, Group
from .forms import Userform
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from .models import Profile


class UserCreate(CreateView):
    template_name = 'core/form.html'
    form_class = Userform
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        group = get_object_or_404(Group, name='Veterinários')
        url = super().form_valid(form)

        self.object.groups.add(group)
        self.object.save()
        Profile.objects.create(user=self.object)

        return url

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['title_window'] = 'PetVet - Registrar Usúario'
        context['title_page'] = 'Registrar Usúario'
        context['tips'] = 'Preencha os campos para registrar um novo usúario.'

        return context


class ProfileUpdate(UpdateView):
    template_name = 'core/form.html'
    model = Profile
    fields = ['name', 'cpf', 'phone']
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Profile, user=self.request.user)
        return self.object

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['title_window'] = 'PetVet - Meus Dados'
        context['title_page'] = 'Meus Dados Cadastrados'
        context['tips'] = 'Preencha os campos para completar seu perfil.'

        return context
