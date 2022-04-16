from django.db import models
from django.urls import reverse
from datetime import date

castrated_status = (('Não', 'Não'), ('Sim', 'Sim'))
sex_status = (('Macho', 'Macho'), ('Fêmea', 'Fêmea'))
procedures = (('Consulta', 'Consulta'), ('Retorno', 'Retorno'),
              ('Exame', 'Exame'), ('Cirurgia', 'Cirurgia'))
type_sedative = (('Não', 'Não'), ('Simples', 'Simples'),
                 ('Complexo', 'Complexo'))


class Tutor(models.Model):
    """Model representing a classe Tutor."""
    tutor_name = models.CharField(
        max_length=30, verbose_name='Nome do Tutor')
    cpf = models.CharField(max_length=14, null=True,
                           verbose_name='CPF')
    phone = models.CharField(max_length=15, null=True,
                             verbose_name='Telefone')
    email = models.EmailField(max_length=254, verbose_name='Email')
    cep = models.CharField(max_length=9, verbose_name='Cep')
    street = models.CharField(max_length=40, verbose_name='Rua')
    number = models.IntegerField(verbose_name='Numero')
    district = models.CharField(max_length=40, verbose_name='Bairro')
    city = models.CharField(
        max_length=40, default='Petrolina', verbose_name='Cidade')
    state = models.CharField(
        max_length=40, default='Pernambuco', verbose_name='Estado')

    class Meta:
        ordering = ['tutor_name']

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
        max_length=30, verbose_name='Nome do Pet')
    species = models.CharField(
        max_length=20, verbose_name='Espécie')
    breed = models.CharField(
        max_length=30, verbose_name='Raça')
    gender = models.CharField(
        max_length=5, choices=sex_status, verbose_name='Genêro')
    date_of_birth = models.DateField(
        null=True, blank=True, verbose_name='Data de Nascimento')
    castrated = models.CharField(
        max_length=3, choices=castrated_status, default='N', verbose_name='Castrado?')
    weight = models.DecimalField(
        max_digits=6, decimal_places=3, verbose_name='Peso')
    tutor_name = models.ForeignKey(
        'Tutor', on_delete=models.PROTECT, null=True, verbose_name="Nome do Tutor")

    class Meta:
        ordering = ['-id']

    def get_absolute_url(self):
        """Returns the url to access a particular pet instance."""
        return reverse('pet-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return self.pet_name


class Vet(models.Model):
    """Model representing a classe Vet."""
    vet_name = models.CharField(
        max_length=30, verbose_name='Nome')

    class Meta:
        ordering = ['vet_name']

    def __str__(self):
        """String for representing the Model object."""
        return self.vet_name


class MedicalCare(models.Model):
    """Model representing a classe Medical care."""
    id = models.AutoField(primary_key=True)
    date = models.DateField(default=date.today, verbose_name='Data')
    time = models.TimeField(verbose_name='Hora')
    pet_name = models.ForeignKey(
        'Pets', on_delete=models.PROTECT, null=True, verbose_name='Nome do Pet')
    procedure = models.CharField(
        max_length=8, choices=procedures, verbose_name='Tipo de atendimento')
    vet_name = models.ForeignKey(
        'Vet', on_delete=models.PROTECT, null=True, verbose_name='Veterinario')
    sedative = models.CharField(
        max_length=8, choices=type_sedative, default='Não', verbose_name='Tipo de sedativo')
    report = models.TextField(
        max_length=1000, verbose_name='Relato do problema')

    class Meta:
        ordering = ['-date']

    def get_absolute_url(self):
        """Returns the url to access a particular medical care instance."""
        return reverse('medical_care_detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.procedure} - {self.pet_name} - {self.date}'
