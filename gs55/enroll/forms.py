from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django import forms
class SignUpForm(UserCreationForm):
    password2 = forms.CharField(label="enter password again",widget = forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']  
        labels = {'email':"Email"}

class EditUserProfileForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','date_joined','last_login','is_active']
        labels = {'email':'Email'} 
        

class EditAdminForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = '__all__'
        labels = {'email':'Email'} 

