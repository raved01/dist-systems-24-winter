from django.db import models

# Create your models here.
# app_name/models.py
from django.db import models

class ModelName(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
