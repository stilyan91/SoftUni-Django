from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import BaseUserManager, PermissionsMixin
from django.contrib.auth.models import AbstractUser, User, AbstractBaseUser
from django.db import models


# change behavior of the current table
# class AppUserCurrent(User):
#     class Meta:
#         proxy = True
#         # ordering = ('first_name')

    # def some_behavior(self)...

# class MyCustomUser(AbstractUser):
#   birthday = models.DateField()

# One-To-one relationship
# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)


class AppUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not email:
            raise ValueError("The given username must be set")

        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self,  email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)



# Extending AbstractBaseUser
class AppUser(AbstractBaseUser, PermissionsMixin):
    USERNAME_FIELD = 'email'
    objects = AppUserManager()
    email = models.EmailField(unique=True, null=False, blank=False)
    is_staff = models.BooleanField(default=False)



