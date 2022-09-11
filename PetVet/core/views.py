from .models import MedicalCare, Pets, Tutor, Vet, GeneralClinic, PhysicalExam, GeneralDhermExam
from braces.views import GroupRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView, TemplateView


# Views Index
class IndexView(TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        num_pets = Pets.objects.all().count()
        num_tutors = Tutor.objects.all().count()
        num_medical_cares = MedicalCare.objects.all().count()
        num_general_clinics = GeneralClinic.objects.all().count()
        num_physical_exams = PhysicalExam.objects.all().count()

        context['num_pets'] = num_pets
        context['num_tutors'] = num_tutors
        context['num_medical_cares'] = num_medical_cares
        context['num_general_clinics'] = num_general_clinics
        context['num_physical_exams'] = num_physical_exams

        return context


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

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['title_window'] = 'PetVet - Novo Cadastro'
        context['title_page'] = 'Novo Cadastro'
        context['tips'] = 'Preencha os campos para criar um novo atendimento.'

        return context


class MedicalCareUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = MedicalCare
    fields = ['date', 'time', 'pet_name',
              'procedure', 'vet_name', 'sedative', 'report']
    template_name = 'core/form.html'
    success_url = reverse_lazy('medical_cares')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['title_window'] = 'PetVet - Editar Cadastro'
        context['title_page'] = 'Editar Cadastro'
        context['tips'] = 'Preencha os campos para editar esse atendimento.'

        return context


class MedicalCareDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = [u'Recepcionista', u'Admin']
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

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['title_window'] = 'PetVet - Novo Cadastro'
        context['title_page'] = 'Novo Cadastro'
        context['tips'] = 'Preencha os campos para criar um novo cadastro.'

        return context


class PetUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Pets
    fields = ['pet_name', 'species', 'breed', 'gender',
              'date_of_birth', 'castrated', 'weight', 'tutor_name']
    template_name = 'core/form.html'
    success_url = reverse_lazy('pets')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['title_window'] = 'PetVet - Editar Cadastro'
        context['title_page'] = 'Editar Cadastro'
        context['tips'] = 'Preencha os campos para editar esse cadastro.'

        return context


class PetDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = [u'Recepcionista', u'Admin']
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

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['title_window'] = 'PetVet - Novo Cadastro'
        context['title_page'] = 'Novo Cadastro'
        context['tips'] = 'Preencha os campos para criar um novo cadastro.'

        return context


class TutorUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Tutor
    fields = ['tutor_name', 'cpf', 'phone', 'email', 'cep',
              'street', 'number', 'district', 'city', 'state']
    template_name = 'core/form.html'
    success_url = reverse_lazy('tutors')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['title_window'] = 'PetVet - Editar Cadastro'
        context['title_page'] = 'Editar Cadastro'
        context['tips'] = 'Preencha os campos para editar esse cadastro.'

        return context


class TutorDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = [u'Recepcionista', u'Admin']
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

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['title_window'] = 'PetVet - Novo Cadastro'
        context['title_page'] = 'Novo Cadastro'
        context['tips'] = 'Preencha os campos para criar um novo cadastro.'

        return context


class VetUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Vet
    fields = ['vet_name']
    template_name = 'core/form.html'
    success_url = reverse_lazy('vets')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['title_window'] = 'PetVet - Editar Cadastro'
        context['title_page'] = 'Editar Cadastro'
        context['tips'] = 'Preencha os campos para editar esse cadastro.'

        return context


class VetDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = [u'Recepcionista', u'Admin']
    model = Vet
    template_name = 'core/form_delete.html'
    success_url = reverse_lazy('vets')


# Views General Clinic
class GeneralClinicList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = GeneralClinic
    template_name = 'core/general_clinic_list.html'


class GeneralClinicDetail(LoginRequiredMixin, DetailView):
    login_url = reverse_lazy('login')
    model = GeneralClinic
    template_name = 'core/general_clinic_detail.html'
    success_url = reverse_lazy('general_clinics')


class GeneralClinicCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = GeneralClinic
    fields = ['medical_care', 'choice_anamnese',
              'anamnese', 'choice_anti_rabica', 'choice_type_v', 'choice_v', 'choice_type_felina', 'choice_felina', 'others_felina', 'choice_verminose', 'others_verminose', 'choice_ectopas', 'others_ectopas', 'choice_leish']
    template_name = 'core/form.html'
    success_url = reverse_lazy('physical_exam_new')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['title_window'] = 'PetVet - Exame Clínico Geral'
        context['title_page'] = 'Novo Exame Clínico Geral'
        context['tips'] = 'Preencha os campos para criar um novo exame clínico geral.'

        return context


class GeneralClinicUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = GeneralClinic
    fields = ['medical_care', 'choice_anamnese',
              'anamnese', 'choice_anti_rabica', 'choice_type_v', 'choice_v', 'choice_type_felina', 'choice_felina', 'others_felina', 'choice_verminose', 'others_verminose', 'choice_ectopas', 'others_ectopas', 'choice_leish']
    template_name = 'core/form.html'
    success_url = reverse_lazy('general_clinics')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['title_window'] = 'PetVet - Editar Exame Clínico Geral'
        context['title_page'] = 'Editar Exame Clínico Geral'
        context['tips'] = 'Preencha os campos para editar esse exame.'

        return context


class GeneralClinicDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = [u'Recepcionista', u'Admin']
    model = GeneralClinic
    template_name = 'core/form_delete.html'
    success_url = reverse_lazy('general_clinics')


# Views Physical Exam
class PhysicalExamList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = PhysicalExam
    template_name = 'core/physical_exam_list.html'


class PhysicalExamDetail(LoginRequiredMixin, DetailView):
    login_url = reverse_lazy('login')
    model = PhysicalExam
    template_name = 'core/physical_exam_detail.html'
    success_url = reverse_lazy('physical_exams')


class PhysicalExamCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = PhysicalExam
    fields = ['medical_care', 'choice_conduct',
              'weight', 'choice_consciousness', 'stance', 'hydration', 'choice_nutricional_status', 'oculopalpebral', 'bucal', 'genital', 'choice_dental_calculus', 'choice_dental_loss', 'gengivite', 'choice_ulcera', 'choice_halitose', 'linfonodos', 'fc', 'fr', 'tpc', 'tr', 'pulse', 'choice_auscu_cardio', 'heart_rate', 'choice_auscu_pulmonar', 'choice_percu_pulmonar', 'palpa_abdominal', 'choice_mamas', 'choice_nodulo', 'choice_nodulo_pain', 'choice_local_pain', 'choice_pain_m', 'genital_region', 'choice_ectoparasitas', 'ectoparasitas_intensity', 'pelage', 'ears', 'diag_differ', 'diag_final', 'case_classification']
    template_name = 'core/form.html'
    success_url = reverse_lazy('physical_exams')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['title_window'] = 'PetVet - Exame Fisico Geral'
        context['title_page'] = 'Novo Exame Fisico Geral'
        context['tips'] = 'Preencha os campos para criar um novo exame fisico geral.'

        return context


class PhysicalExamUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = PhysicalExam
    fields = ['medical_care', 'choice_conduct',
              'weight', 'choice_consciousness', 'stance', 'hydration', 'choice_nutricional_status', 'oculopalpebral', 'bucal', 'genital', 'choice_dental_calculus', 'choice_dental_loss', 'gengivite', 'choice_ulcera', 'choice_halitose', 'linfonodos', 'fc', 'fr', 'tpc', 'tr', 'pulse', 'choice_auscu_cardio', 'heart_rate', 'choice_auscu_pulmonar', 'choice_percu_pulmonar', 'palpa_abdominal', 'choice_mamas', 'choice_nodulo', 'choice_nodulo_pain', 'choice_local_pain', 'choice_pain_m', 'genital_region', 'choice_ectoparasitas', 'ectoparasitas_intensity', 'pelage', 'ears', 'diag_differ', 'diag_final', 'case_classification']
    template_name = 'core/form.html'
    success_url = reverse_lazy('physical_exams')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['title_window'] = 'PetVet - Editar Exame Fisico Geral'
        context['title_page'] = 'Editar Exame Fisico Geral'
        context['tips'] = 'Preencha os campos para editar esse exame.'

        return context


class PhysicalExamDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = [u'Recepcionista', u'Admin']
    model = PhysicalExam
    template_name = 'core/form_delete.html'
    success_url = reverse_lazy('physical_exams')


# Views General Dherm Exam
class GeneralDhermCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = GeneralDhermExam
    fields = ['medical_care', 'report', 'choice_anamnese',
              'evolution_time', 'choice_evolution_status', 'evolution_score', 'quest_01_where_begin', 'quest_02_how_are_lesions', 'prurido', 'prurido_intensity', 'choice_prurido', 'quest_03_prurido_history', 'quest_04_recent_medical_care', 'quest_05_aplication_prescrition_topic', 'quest_06_feels_better_topic', 'quest_07_feels_intensity_topic', 'quest_08_aplication_prescrition_oral', 'quest_09_feels_better_oral', 'quest_10_feels_intensity_oral', 'quest_11_aplication_prescrition_oral',
              'quest_12_aplication_prescrition_oral', 'quest_13_color_skin',
              'quest_14_color_fur', 'quest_15_dermatopias',
              'quest_16_persons_dermatopias', 'quest_16_persons_dermatopias', 'quest_17_contacts', 'quest_18_contacts_quant', 'quest_19_contacts_assint', 'quest_20_contacts_sint_quant', 'quest_21_contacts_sint_period', 'quest_22_contacts_access_street', 'quest_23_contacts_sleep_local', 'quest_24_contacts_petbed', 'quest_25_contacts_wash_petbed', 'quest_26_contacts_grass_earth', 'quest_27_contacts_plants', 'quest_28_special_place', 'quest_29_travel_cities', 'quest_30_pulgas_carrapatos']
    template_name = 'core/form.html'
    success_url = reverse_lazy('physical_exams')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['title_window'] = 'PetVet - Exame Dermatológico Geral'
        context['title_page'] = 'Novo Exame Dermatológico Geral'
        context['tips'] = 'Preencha os campos para criar um novo exame Dermatólogico geral.'

        return context
