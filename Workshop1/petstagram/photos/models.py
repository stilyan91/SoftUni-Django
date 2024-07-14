from django.core.validators import MinLengthValidator
from django.db import models

from petstagram.pets.models import Pet
from petstagram.photos.validators import validate_max_size


# Create your models here.


class Photo(models.Model):
    photo = models.ImageField(validators=[validate_max_size])
    description = models.TextField(max_length=300, validators=[MinLengthValidator(10)], null=True, blank=True)
    location = models.CharField(max_length=30, blank=True, null=True)
    tagged_pet = models.ManyToManyField(to=Pet, blank=True)
    date_of_publication = models.DateTimeField(auto_now=True)

