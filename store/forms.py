from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import *
from django.contrib.auth import authenticate

class CreateUserForm(UserCreationForm):
	class Meta:
	  model = User
	  fields = ['first_name','last_name','username', 'email', 'password1', 'password2']


class presUpForm(forms.ModelForm):
	class Meta:
		model = Prescription
		fields = ['precripImage']

class presUpGForm(forms.ModelForm):
	class Meta:
		model = Patient
		fields = ['name', 'email']