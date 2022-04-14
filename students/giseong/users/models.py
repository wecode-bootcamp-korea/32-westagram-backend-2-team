from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class User(models.Model):
    user_name         = models.CharField(max_length=20)
    user_email        = models.EmailField(max_length=128, null=False, unique=True)
    user_password     = models.CharField(max_length=128, null=False)
    user_phone_number = models.CharField(max_length=12, unique=True)

    class Meta:
        db_table = 'users'