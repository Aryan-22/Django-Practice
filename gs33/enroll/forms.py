from django import forms
class StudentRegistration(forms.Form):
   #name = forms.CharField(min_length=2,max_length=10)
    name = forms.CharField(error_messages={"required":"Enter your Name"},empty_value="Aryan")
    check = forms.BooleanField(label="I agree")
    roll = forms.IntegerField(min_value=5)
    price = forms.DecimalField(min_value=4,max_value=1000,max_digits=3)
    rate =  forms.FloatField(required=False)
    email = forms.EmailField(min_length = 5,max_length=10)
    website = forms.URLField()
    comment = forms.SlugField(allow_unicode=False, required=False)
    password = forms.CharField(widget = forms.PasswordInput)
    description = forms.CharField(widget = forms.Textarea)
    feedback = forms.CharField(widget=forms.Textarea(attrs={'rows':3,'cols':50}))