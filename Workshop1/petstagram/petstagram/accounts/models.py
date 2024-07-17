from enum import Enum

from django.core.validators import MinLengthValidator
from django.db import models
from django.contrib.auth import models as auth_models


class ChoicesMixin:
    @classmethod
    def choices(cls):
        return [(choice.value, choice.name) for choice in cls]

class ChoicesStringMixin(ChoicesMixin):
    @classmethod
    def max_length(cls):
        return max(len(x.value) for x in cls)


class Gender(ChoicesStringMixin, Enum):
    MALE = 'male'
    FEMALE = 'female'
    DO_NOT_SHOW = 'do not show'

    @classmethod
    def choices(cls):
        return [(choice.value, choice.name) for choice in cls]


def validate_only_alphabetical(value):
    for char in value:
        if not char.isalpha():
            return False
    return True


class PetstagramUser(auth_models.AbstractUser):
    FIRST_NAME_MIN_LENGTH = 2
    FIRST_NAME_MAX_LENGTH = 30
    LAST_NAME_MIN_LENGTH = 2
    LAST_NAME_MAX_LENGTH = 30

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(MinLengthValidator(FIRST_NAME_MIN_LENGTH),
                    validate_only_alphabetical))

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=(MinLengthValidator(LAST_NAME_MIN_LENGTH),
                    validate_only_alphabetical))

    email = models.EmailField(unique=True)
    gender = models.CharField(choices=Gender.choices(), max_length=Gender.max_length())
    profile_picture = models.URLField(blank=True, null=True)
