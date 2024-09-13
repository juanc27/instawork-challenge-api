from django.db import models

# Create your models here.
class Member(models.Model):
    VALID_ROLES = (
        ('admin', 'Admin'),
        ('regular', 'Regular User')
    )
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    phone = models.CharField(max_length=12, unique=True)
    role = models.CharField(max_length=255, choices=VALID_ROLES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        if self.role not in [choice[0] for choice in self.VALID_ROLES]:
            raise ValidationError(
                f'Invalid value for role: {self.role}. Must be one of: {", ".join([choice[0] for choice in self.VALID_ROLES])}'
            )
