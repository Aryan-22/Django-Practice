from django.db import models
from django.contrib.auth.models import User
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    desc = models.TextField()
# Create your models here.
