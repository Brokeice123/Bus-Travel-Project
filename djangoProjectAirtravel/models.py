from django.db import models


class Traveller(models.Model):
    name = models.CharField(max_length=20, blank=True, null=False)
    email = models.EmailField(max_length=20, blank=True, null=False)
    phone = models.IntegerField(max_length=20, blank=True, null=False)
    origin = models.CharField(max_length=20, blank=True, null=False)
    destination = models.CharField(max_length=20, blank=True, null=False)
    payment = models.CharField(max_length=20, blank=True, null=False)


def __str__(self):
    return self.name
