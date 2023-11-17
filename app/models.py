from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    second_name = models.CharField(max_length=150, verbose_name="Отчество")
    image = models.ImageField(upload_to="avatar", max_length=1000)

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.second_name}'

class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    price = models.DecimalField(verbose_name="Цена", max_digits=10, decimal_places=2)