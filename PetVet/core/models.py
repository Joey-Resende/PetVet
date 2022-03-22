import uuid
from cpf_field.models import CPFField
from django.db import models
from django.urls import reverse
from phone_field import PhoneField

castrated_status = (('N', 'Não'), ('S', 'Sim'))
sex_status = (('M', 'Macho'), ('F', 'Fêmea'))
procedures = (('C', 'Consulta'), ('R', 'Retorno'),
              ('E', 'Exame'), ('C', 'Cirurgia'))
type_sedative = (('N', 'Nao'), ('S', 'Simples'), ('C', 'Complexo'))


class Pets(models.Model):
    """Model representing a classe pet."""
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, help_text='Id do Pet')
    pet_name = models.CharField(
        max_length=30, help_text='Digite o nome do Pet')
    species = models.CharField(
        max_length=20, help_text='Digite a espécie do Pet')
    breed = models.CharField(
        max_length=30, help_text='Digite a raça do Pet')
    gender = models.CharField(
        max_length=1, choices=sex_status, blank=True, help_text='Escolha o genêro do Pet')
    date_of_birth = models.DateField(
        null=True, blank=True, help_text='Digite a data de nascimento do Pet')
    castrated = models.CharField(
        max_length=1, choices=castrated_status, blank=True, default='N', help_text='Escolha se o Pet e castrado')
    weight = models.DecimalField(
        max_digits=6, decimal_places=3, help_text='Digite o peso do Pet')

    class Meta:
        ordering = ['id']

    def get_absolute_url(self):
        """Returns the url to access a particular pet instance."""
        return reverse('pet-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return self.species


class Tutor(models.Model):
    """Model representing a classe Tutor."""
    tutor_name = models.CharField(
        max_length=30, help_text='Digite o nome do Tutor')
    cpf = CPFField('cpf')
    phone = PhoneField(blank=True, help_text='Digite seu telefone')
    email = models.EmailField(max_length=254, help_text='Digite seu Email')
    street = models.CharField(max_length=40, help_text='Digite a rua')
    number = models.IntegerField(help_text='Digite o numero')
    district = models.CharField(max_length=40, help_text='Digite a rua')
    state = models.CharField(max_length=40, help_text='Digite a rua')
    cep = models.IntegerField(help_text='Digite o cep')


class MedicalCare(models.Model):
    """Model representing a classe Medical care."""
    date = models.DateField(null=True, blank=True,
                            help_text='Data do atendimento')
    time = models.TimeField(help_text='Hora do atendimento')
    procedure = models.CharField(
        max_length=1, choices=procedures, blank=True, help_text='Escolha o tipo do atendimento')
    sedative = models.CharField(
        max_length=1, choices=type_sedative, blank=True, help_text='Escolha o tipo de sedativo')
    report = models.TextField(
        max_length=1000, blank=True, help_text='Relato do problema')


class Vet(models.Model):
    """Model representing a classe Vet."""
    vet_name = models.CharField(
        max_length=30, help_text='Nome do Veterinario')
