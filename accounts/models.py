from djongo import models
from django.contrib.auth.hashers import make_password


# Create your models here.
class CustomUser(models.Model):
    MALE, FEMALE = 'male', 'female'
    ADMIN, USER = 'admin', 'user'
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female')
    )
    ROLE_CHOICES = (
        (ADMIN, 'Admin'),
        (USER, 'User')
    )

    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=15, unique=True)
    city = models.CharField(max_length=32)
    password = models.CharField(max_length=256)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=8, default=MALE)
    role = models.CharField(choices=ROLE_CHOICES, max_length=8, default=USER)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.email

