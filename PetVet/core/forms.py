from django import forms
from .models import MedicaCare, Pets, Tutor
from .models import PhysicalExam, GeneralClinic, GeneralDhermExam
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


class GeneralDhermExamForm(forms.ModelForm):
    class Meta:
        model = GeneralDhermExam
        fields = ['medical_care', 'report', 'choice_anamnese',
                  'evolution_time', 'choice_evolution_status', 'evolution_score', 'quest_01_where_begin', 'quest_02_how_are_lesions', 'prurido', 'prurido_intensity', 'choice_prurido', 'quest_03_prurido_history', 'quest_04_recent_medical_care', 'quest_05_aplication_prescrition_topic', 'quest_06_feels_better_topic', 'quest_07_feels_intensity_topic', 'quest_08_aplication_prescrition_oral', 'quest_09_feels_better_oral', 'quest_10_feels_intensity_oral', 'quest_11_aplication_prescrition_oral',
                  'quest_12_aplication_prescrition_oral', 'quest_13_color_skin',
                  'quest_14_color_fur', 'quest_15_dermatopias',
                  'quest_16_persons_dermatopias', 'quest_17_contacts', 'quest_18_contacts_quant', 'quest_19_contacts_assint', 'quest_20_contacts_sint_quant', 'quest_21_contacts_sint_period', 'quest_22_contacts_access_street', 'quest_23_contacts_sleep_local', 'quest_24_contacts_petbed', 'quest_25_contacts_wash_petbed', 'quest_26_contacts_grass_earth', 'quest_27_contacts_plants', 'quest_28_special_place', 'quest_29_travel_cities', 'quest_30_pulgas_carrapatos', 'quest_31_previne_carrapatos', 'quest_32_dose_freq', 'quest_33_food', 'quest_34_food_switch_freq', 'quest_35_food_diet_time', 'quest_36_water_offer', 'quest_37_homemade_food', 'quest_38_diarr', 'quest_39_diarr_food', 'quest_40_diarr_saz', 'quest_41_material_things', 'quest_42_solar_time', 'quest_43_feels_cold', 'quest_44_is_active', 'quest_45_hipoativo', 'quest_46_agitado', 'quest_47_anxietys', 'quest_48_anxiety_travel', 'quest_49_wound_get_worse', 'quest_50_family_change', 'quest_51_family_change_affinity', 'quest_52_family_change_house', 'quest_53_restrict_area_stay', 'quest_54_restrict_walk_play', 'quest_55_others_changes', 'quest_56_lick_ends', 'quest_57_stay_alone']
