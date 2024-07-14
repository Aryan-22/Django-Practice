from django import forms
from django.core import validators
from .models import User
class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name','email','password']
        labels = {"name":"Enter name","password":"Enter password","email":"Enter email"}
        error_messages = {
            "name":{"required":"Name is must!"},
            "password":{"required":"Password is needed"}
        }
        widgets = {
            'password':forms.PasswordInput,
            'name':forms.TextInput(attrs={'class':'myclass','placeholder':"aryan"})
        }
        


      