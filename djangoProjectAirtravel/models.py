from django.db import models


class Traveller(models.Model):
    name = models.CharField(max_length=20, blank=True, null=False)
    email = models.EmailField(max_length=20, blank=True, null=False)
    phone = models.IntegerField(max_length=20, blank=True, null=False)
    origin = models.CharField(max_length=20, blank=True, null=False)
    destination = models.CharField(max_length=20, blank=True, null=False)
    seat = models.IntegerField(max_length=20, blank=True, null=False, default=1)
    id_number = models.IntegerField(max_length=20, blank=True, null=False, default=1234523)
    amount = models.IntegerField(max_length=20, blank=True, null=False, default=1000)


def __str__(self):
    return self.name
