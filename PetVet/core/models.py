import uuid
from django.db import models
from django.urls import reverse

castrated_status = (('N', 'Nao'), ('S', 'Sim'))
sex_status = (('M', 'Macho'), ('F', 'Femea'))


class Pets(models.Model):
    """Model representing a classe pet."""
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, help_text='Id for Pet')
    pet_name = models.CharField(
        max_length=30, help_text='Enter a name of pet')
    species = models.CharField(
        max_length=20, help_text='Enter a name of species')
    breed = models.CharField(
        max_length=30, help_text='Enter a name of a animal breed')
    gender = models.CharField(
        max_length=1, choices=sex_status, blank=True, help_text='Enter a gender of a animal')
    date_of_birth = models.DateField(null=True, blank=True)
    castrated = models.CharField(
        max_length=1, choices=castrated_status, blank=True, default='N', help_text='')
    weight = models.FloatField()

    class Meta:
        ordering = ['id']

    def get_absolute_url(self):
        """Returns the url to access a particular pet instance."""
        return reverse('pet-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return self.species
