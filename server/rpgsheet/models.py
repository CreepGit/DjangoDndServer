from django.db import models

# Create your models here.
class CharacterInformation(models.Model):
    data = models.TextField()
    key = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)

