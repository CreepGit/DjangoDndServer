from django.db import models
from django.utils.timezone import now
# Create your models here.
class CharacterInformation(models.Model):
    data = models.TextField()
    key = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=30, blank=True)
