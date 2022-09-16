from django import forms
from .models import PhysicalExam, MedicaCare, Pets, Tutor
from .models import GeneralClinic
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit


class MedicalCareForm(forms.ModelForm):
    class Meta:
        model = MedicaCare
        fields = ['date', 'time', 'pet_name',
              'procedure', 'vet_name', 'sedative', 'report']


class PetForm(forms.ModelForm):
    class Meta:
        model = Pets
        fields = ['pet_name', 'species', 'breed', 'gender',
              'date_of_birth', 'castrated', 'weight', 'tutor_name']


class TutorForm(forms.ModelForm):
    class Meta:
        model = Tutor
        fields = ['tutor_name', 'cpf', 'phone', 'email', 'cep',
              'street', 'number', 'district', 'city', 'state']


class GeneralClinicForm(forms.ModelForm):
    class Meta:
        model = GeneralClinic
        fields = ['medical_care', 'choice_anamnese',
              'anamnese', 'choice_anti_rabica', 'choice_type_v', 'choice_v', 'choice_type_felina', 'choice_felina', 'others_felina', 'choice_verminose', 'others_verminose', 'choice_ectopas', 'others_ectopas', 'choice_leish']


class PhysicalExamForm(forms.ModelForm):
    class Meta:
        model = PhysicalExam
        fields = ['medical_care', 'choice_conduct',
              'weight', 'choice_consciousness', 'stance', 'hydration', 'choice_nutricional_status', 'oculopalpebral', 'bucal', 'genital', 'choice_dental_calculus', 'choice_dental_loss', 'gengivite', 'choice_ulcera', 'choice_halitose', 'linfonodos', 'fc', 'fr', 'tpc', 'tr', 'pulse', 'choice_auscu_cardio', 'heart_rate', 'choice_auscu_pulmonar', 'choice_percu_pulmonar', 'palpa_abdominal', 'choice_mamas', 'choice_nodulo', 'choice_nodulo_pain', 'choice_local_pain', 'choice_pain_m', 'genital_region', 'choice_ectoparasitas', 'ectoparasitas_intensity', 'pelage', 'ears', 'diag_differ', 'diag_final', 'case_classification']
     