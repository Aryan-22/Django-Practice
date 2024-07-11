from django import forms
from django.core import validators
class StudentRegistration(forms.Form):
   #name = forms.CharField(min_length=2,max_length=10)
   name = forms.CharField(validators=[validators.MaxLengthValidator(10)])
   email = forms.EmailField()
   password = forms.CharField(widget = forms.PasswordInput)
   repassword = forms.CharField(widget = forms.PasswordInput)

   def clean(self):
      cleaned_data = super().clean()
      p = cleaned_data['password']
      rp = cleaned_data['repassword']
      if rp != p:
         raise forms.ValidationError("passwords entered are not matching !")

      