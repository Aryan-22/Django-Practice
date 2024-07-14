from django import forms
from django.core import validators
from .models import User
class StudentRegistration(forms.ModelForm):
    name = forms.CharField(max_length=50)
    class Meta:
        model = User
        fields = ['name','email','password']
        labels = {"name":"Enter name","password":"Enter password","email":"Enter email"}

        widgets = {
            'password':forms.PasswordInput
        }
        


      