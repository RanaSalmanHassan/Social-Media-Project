from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email','password1','password2')

class Edit_Proifle_Form(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)
