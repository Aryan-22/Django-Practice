from django.db import models
class User(models.Model):
    student_name = models.CharField(max_length=50)
    teacher_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length= 100)
# Create your models here.
