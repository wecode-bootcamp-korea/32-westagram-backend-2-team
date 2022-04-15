from django.db import models

# Create your models here.
class User(models.Model):
    name         = models.CharField(max_length=20)
    email        = models.EmailField(max_length=128, null=True, unique=True)
    password     = models.CharField(max_length=128, null=True)
    phone_number = models.CharField(max_length=12, unique=True)

    class Meta:
        db_table = 'users'