from django import forms
class StudentRegistration(forms.Form):
   #name = forms.CharField(min_length=2,max_length=10)
   name = forms.CharField()
   email = forms.EmailField()
   password = forms.CharField(widget = forms.PasswordInput)
   def clean_name(self):
      var = self.cleaned_data["name"]
      if len(var) < 4:
         raise forms.ValidationError("Enter more than or equal to 4 char")
      return var