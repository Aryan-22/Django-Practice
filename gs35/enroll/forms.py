from django import forms
class StudentRegistration(forms.Form):
   #name = forms.CharField(min_length=2,max_length=10)
   name = forms.CharField()
   email = forms.EmailField()

   def clean(self):
      cleaned_data = super().clean()
      val_name = self.cleaned_data['name']
      val_email = self.cleaned_data['email']
      if len(val_name) < 4:
         raise forms.ValidationError("Enter more than or equal to 4 chars")
      if len(val_email) < 10:
         raise forms.ValidationError("Enter more than or equal to 10 chars")
      