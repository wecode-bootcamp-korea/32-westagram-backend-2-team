from django.db import models

# Create your models here.

class Uesr(models.Model) :
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=150)
    password = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=12)

    class Meta :
        db_table = 'users'