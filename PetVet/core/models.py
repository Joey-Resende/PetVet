from django.db import models
from django.urls import reverse


class SpeciesOfPet(models.Model):
    """Model representing a pet species (e.g. cat or dog)."""
    species = models.CharField(
        max_length=200, help_text='Enter a pet species (e.g. cat or dog)')

    def __str__(self):
        """String for representing the Model object."""
        return self.species


class Procedures(models.Model):
    """Model representing a procedure (but not a specific copy of a book)."""
    procedure = models.CharField(max_length=200)
    doctor = models.ForeignKey('Doctor', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(
        max_length=1000, help_text='Enter a brief description of procedure')
    species = models.ManyToManyField(
        SpeciesOfPet, help_text='Select a species for this pet')

    def __str__(self):
        """String for representing the Model object."""
        return self.procedure

    def get_absolute_url(self):
        """Returns the url to access a detail record for this procedure."""
        return reverse('procedure-detail', args=[str(self.id)])


class Doctor(models.Model):
    """Model representing a doctor."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """Returns the url to access a particular doctor instance."""
        return reverse('doctor-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'
