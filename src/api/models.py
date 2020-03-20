import uuid

from django.db import models


# Create your models here.
class filesModel(models.Model):
    file = models.FileField(blank=False, null=False)
    hash = models.CharField(max_length=255, blank=False, null=True)

    def __str__(self):
        return self.hash


class userData(models.Model):
    id = models.AutoField(primary_key=True)
    transactionHash = models.UUIDField(max_length=255, null=False, default=uuid.uuid4, editable=False)
    userId = models.IntegerField(unique=True, null=False)
    first_name = models.CharField(max_length=255, null=False, blank=False)
    middle_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=False, blank=False)
    date = models.DateField(blank=False)
    phoneNumber = models.IntegerField(blank=True, null=True)
