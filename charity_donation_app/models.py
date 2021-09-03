from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

# Create your models here.

TYPES = {
    (1, "Fundacja"),
    (2, "Organizacja Pozarządowa"),
    (3, "Zbiórka Lokalna"),
}


class User(AbstractUser):
    pass


class Category(models.Model):
    name = models.CharField(max_length=64, verbose_name="Kategoria")

    def __str__(self):
        return self.name


class Institution(models.Model):
    name = models.CharField(max_length=64, verbose_name="Nazwa instytucji")
    description = models.TextField()
    type = models.CharField(max_length=64, choices=TYPES, default=1)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return f"{self.name}, {self.type}"


class Donation(models.Model):
    categories = models.ManyToManyField(Category)
    quantity = models.IntegerField(verbose_name="Liczba worków")
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    address = models.CharField(max_length=64, verbose_name="Ulica")
    city = models.CharField(max_length=64, verbose_name="Miasto")
    phone_number = models.IntegerField(null=True, verbose_name="Nr tel.")
    zip_code = models.CharField(max_length=6, verbose_name="Kod pocztowy")
    pick_up_date = models.DateField(verbose_name="Data odbioru")
    pick_up_time = models.TimeField(verbose_name="Godzina odbioru")
    pick_up_comment = models.CharField(max_length=128, verbose_name="Zostaw komentarz")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.city}, {self.quantity}, {self.institution}"
