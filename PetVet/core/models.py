from cpf_field.models import CPFField
from django.db import models
from django.urls import reverse
from phone_field import PhoneField

castrated_status = (('Não', 'Não'), ('Sim', 'Sim'))
sex_status = (('Macho', 'Macho'), ('Fêmea', 'Fêmea'))
procedures = (('Consulta', 'Consulta'), ('Retorno', 'Retorno'),
              ('Exame', 'Exame'), ('Cirurgia', 'Cirurgia'))
type_sedative = (('Não', 'Não'), ('Simples', 'Simples'),
                 ('Complexo', 'Complexo'))


class Tutor(models.Model):
    """Model representing a classe Tutor."""
    tutor_name = models.CharField(
        max_length=30, help_text='Digite o nome do Tutor')
    cpf = CPFField('cpf')
    phone = PhoneField(blank=True, help_text='Digite seu telefone')
    email = models.EmailField(max_length=254, help_text='Digite seu Email')
    street = models.CharField(max_length=40, help_text='Digite a rua')
    number = models.IntegerField(help_text='Digite o numero')
    district = models.CharField(max_length=40, help_text='Digite o Bairro')
    state = models.CharField(max_length=40, help_text='Digite o Estado')
    cep = models.IntegerField(help_text='Digite o cep')

    def get_absolute_url(self):
        """Returns the url to access a particular pet instance."""
        return reverse('tutor-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return self.tutor_name


class Pets(models.Model):
    """Model representing a classe pet."""
    id = models.AutoField(primary_key=True)
    pet_name = models.CharField(
        max_length=30, help_text='Digite o nome do Pet')
    species = models.CharField(
        max_length=20, help_text='Digite a espécie do Pet')
    breed = models.CharField(
        max_length=30, help_text='Digite a raça do Pet')
    gender = models.CharField(
        max_length=5, choices=sex_status, blank=True, help_text='Escolha o genêro do Pet')
    date_of_birth = models.DateField(
        null=True, blank=True, help_text='Digite a data de nascimento do Pet')
    castrated = models.CharField(
        max_length=3, choices=castrated_status, blank=True, default='N', help_text='Escolha se o Pet e castrado')
    weight = models.DecimalField(
        max_digits=6, decimal_places=3, help_text='Digite o peso do Pet')
    tutor_name = models.ForeignKey(
        'Tutor', on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ['id']

    def get_absolute_url(self):
        """Returns the url to access a particular pet instance."""
        return reverse('pet-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return self.pet_name


class Vet(models.Model):
    """Model representing a classe Vet."""
    vet_name = models.CharField(
        max_length=30, help_text='Nome do Veterinario')

    def get_absolute_url(self):
        """Returns the url to access a particular pet instance."""
        return reverse('vet-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return self.vet_name


class MedicalCare(models.Model):
    """Model representing a classe Medical care."""
    date = models.DateField(null=True, blank=True,
                            help_text='Data do atendimento')
    time = models.TimeField(help_text='Hora do atendimento')
    pet_name = models.ForeignKey('Pets', on_delete=models.SET_NULL, null=True)
    procedure = models.CharField(
        max_length=8, choices=procedures, blank=True, help_text='Escolha o tipo do atendimento')
    vet_name = models.ForeignKey('Vet', on_delete=models.SET_NULL, null=True)
    sedative = models.CharField(
        max_length=8, choices=type_sedative, default='N', blank=True, help_text='Escolha o tipo de sedativo')
    report = models.TextField(
        max_length=1000, blank=True, help_text='Relato do problema')

    def get_absolute_url(self):
        """Returns the url to access a particular pet instance."""
        return reverse('medical_care-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return self.report
