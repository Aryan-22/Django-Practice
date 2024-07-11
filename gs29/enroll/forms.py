from django import forms
class StudentRegistration(forms.Form):
    name = forms.CharField(label="yourname",label_suffix=" ",initial="aryan",required=False,disabled=True,help_text="limit 70 char")
