from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator

# Create your models here.
class Member(models.Model):
    VALID_ROLES = (
        ('admin', 'Admin'),
        ('regular', 'Regular User')
    )
    first_name = models.CharField(max_length=255, validators=[MinLengthValidator(1)])
    last_name = models.CharField(max_length=255, validators=[MinLengthValidator(1)])
    email = models.EmailField(max_length=255, unique=True)
    phone = models.CharField(max_length=12, unique=True, validators=[MinLengthValidator(3)])
    role = models.CharField(max_length=255, choices=VALID_ROLES, validators=[MinLengthValidator(1)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
