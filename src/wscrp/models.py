from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Journal(models.Model):
    nom_journal = models.CharField(max_length=50)
    link_journal = models.URLField(max_length=200)

    def __str__(self):
        return self.nom_journal

# python manage.py makemigrations
# python manage.py migrate