from django.db import models

# Create your models here.


class MyUser(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.IntegerField(unique=True, max_length=11)
