from django.db import models

class User(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=70)
    password = models.CharField(max_length=100)
    def __str__(self):
        return self.name
# Create your models here.
