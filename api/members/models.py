from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.core.validators import RegexValidator

# Create your models here.
class Member(models.Model):
    VALID_ROLES = (
        ('admin', 'Admin'),
        ('regular', 'Regular User')
    )
    first_name = models.CharField(max_length=255, validators=[MinLengthValidator(1)])
    last_name = models.CharField(max_length=255, validators=[MinLengthValidator(1)])
    email = models.EmailField(max_length=255, unique=True)
    phone = models.CharField(max_length=15, unique=True, validators=[RegexValidator(r'^\+?\d{10,15}$', 'Enter a valid phone number: min 10 chars, only numbers and +sign allowed, no hyphens.')])
    role = models.CharField(max_length=255, choices=VALID_ROLES, validators=[MinLengthValidator(1)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
