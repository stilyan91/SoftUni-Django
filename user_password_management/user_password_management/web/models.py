from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class Profile(models.Model):
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)

    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        primary_key=True,
    )


class Book(models.Model):
    # correct:
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    # incorrect
    # profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
