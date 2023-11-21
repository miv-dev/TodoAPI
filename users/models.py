from django.contrib.auth.models import AbstractUser
from django.db import models
from import_export import resources
from simple_history.models import HistoricalRecords


# Create your models here.


class User(AbstractUser):
    avatar = models.ImageField(upload_to="assets/avatars/", blank=True)
    history = HistoricalRecords()
