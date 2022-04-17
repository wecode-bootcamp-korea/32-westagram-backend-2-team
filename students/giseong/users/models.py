from django.db import models

# Create your models here.
class User(models.Model):
    name         = models.CharField(max_length=20)
    email        = models.EmailField(max_length=128, unique=True)
    password     = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=30)
    created_at   = models.DateTimeField(auto_now_add=True)
    updated_at   = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'users'