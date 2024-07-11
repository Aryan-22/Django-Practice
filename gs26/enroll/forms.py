from django import forms
class StudentRegistration(forms.Form):
    name = forms.CharField(initial="Aryan",help_text="30 character only")
    email = forms.EmailField()